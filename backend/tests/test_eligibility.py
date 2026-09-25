import uuid
from fastapi import status


def create_family(client, income=0, district="Madurai", taluk="Madurai North", composition="nuclear", ration_card="green"):
    res = client.post(
        "/families",
        json={
            "composition_type": composition,
            "district": district,
            "taluk": taluk,
            "address": "15, South Masi Street",
            "ration_card_type": ration_card,
            "total_household_income": income,
        },
    )
    assert res.status_code == status.HTTP_201_CREATED
    return res.json()["id"]


def add_person(client, family_id, **kwargs):
    default_payload = {
        "name": "Test Person",
        "age": 30,
        "gender": "female",
        "education_level": "secondary",
        "occupation": "homemaker",
        "marital_status": "married",
        "caste_category": "BC",
        "disability_status": False,
        "special_flags": [],
    }
    default_payload.update(kwargs)
    res = client.post(f"/families/{family_id}/persons", json=default_payload)
    assert res.status_code == status.HTTP_201_CREATED
    return res.json()["id"]


def test_senior_destitute_widow_matches_oap_and_dwp(client):
    """Profile 1: A 62-year-old widow with no income -> should match Old Age Pension AND Destitute Widow Pension."""
    family_id = create_family(client, income=0.00)
    person_id = add_person(
        client,
        family_id,
        name="Meenakshi Ammal",
        age=62,
        gender="female",
        marital_status="widowed",
        special_flags=["destitute", "widow"],
        occupation="unemployed",
    )

    res = client.get(f"/persons/{person_id}/eligibility")
    assert res.status_code == status.HTTP_200_OK
    data = res.json()

    eligible_codes = [s["scheme_code"] for s in data["eligible_schemes"]]
    # Must match Old Age Pension (TN-SW-OAP)
    assert "TN-SW-OAP" in eligible_codes, f"Expected TN-SW-OAP in {eligible_codes}"
    # Must match Destitute Widow Pension (TN-SW-DWP)
    assert "TN-SW-DWP" in eligible_codes, f"Expected TN-SW-DWP in {eligible_codes}"


def test_disabled_daily_wage_worker_matches_disability_not_oap(client):
    """Profile 2: A 30-year-old daily wage worker with physical disability
    -> should match disability-specific schemes but NOT old age pension.
    """
    family_id = create_family(client, income=8000.00)
    person_id = add_person(
        client,
        family_id,
        name="Karthik",
        age=30,
        gender="male",
        occupation="daily_wage",
        marital_status="single",
        disability_status=True,
        disability_type="locomotor",
        special_flags=[],
    )

    res = client.get(f"/persons/{person_id}/eligibility")
    assert res.status_code == status.HTTP_200_OK
    data = res.json()

    eligible_codes = [s["scheme_code"] for s in data["eligible_schemes"]]
    # Should match disability schemes
    assert "TN-SW-DA-AIDS-APPLIANCES" in eligible_codes
    assert "TN-SW-DA-MOTOR-VEHICLE" in eligible_codes

    # Should NOT match Old Age Pension
    assert "TN-SW-OAP" not in eligible_codes


def test_high_income_family_excluded_from_income_threshold_schemes(client):
    """Profile 3: A family with total income above threshold
    -> should be excluded from income-gated schemes even if age/gender match.
    """
    # High income: ₹35,000/month
    family_id = create_family(client, income=35000.00)
    person_id = add_person(
        client,
        family_id,
        name="Radha",
        age=30,
        gender="female",
        marital_status="married",
        occupation="homemaker",
        special_flags=[],
    )

    res = client.get(f"/persons/{person_id}/eligibility")
    assert res.status_code == status.HTTP_200_OK
    data = res.json()

    eligible_codes = [s["scheme_code"] for s in data["eligible_schemes"]]

    # Income-gated schemes must NOT be in eligible list:
    # Sathiyavani Muthu Sewing Machine requires <= 6000
    assert "TN-SW-SEWING-MACHINE" not in eligible_codes
    # KMUT requires <= 20833
    assert "TN-SW-KMUT" not in eligible_codes


def test_partially_eligible_scheme_with_specific_rule_failure(client):
    """Profile 4: Explicit test for partially eligible case.
    A person who matches 2 of 3 conditions should show exactly which condition failed and its threshold.
    """
    family_id = create_family(client, income=4000.00)  # Income <= 10000 matches OAP family rule
    person_id = add_person(
        client,
        family_id,
        name="Sundaram",
        age=45,  # Old Age Pension requires age >= 60, so this rule fails
        gender="male",
        occupation="unemployed",
        marital_status="single",
        special_flags=["destitute"],  # matches OAP destitute rule
    )

    res = client.get(f"/persons/{person_id}/eligibility")
    assert res.status_code == status.HTTP_200_OK
    data = res.json()

    # Old Age Pension should be in partially_eligible_schemes
    partial_schemes = {s["scheme_code"]: s for s in data["partially_eligible_schemes"]}
    assert "TN-SW-OAP" in partial_schemes

    oap_match = partial_schemes["TN-SW-OAP"]
    assert oap_match["matched_rules_count"] == 2
    assert oap_match["total_rules_count"] == 3
    assert len(oap_match["failed_rules"]) == 1

    failed_rule = oap_match["failed_rules"][0]
    assert failed_rule["field_name"] == "age"
    assert failed_rule["expected_value"] == "60"
    assert failed_rule["actual_value"] == "45"
    assert "age is 45, requires >= 60" in failed_rule["reason"]


def test_family_eligibility_endpoint_evaluates_all_members(client):
    """Profile 5: GET /families/{id}/eligibility returns results for all persons in the household."""
    family_id = create_family(client, income=5000.00)

    # Member 1: Elderly grandmother (age 68, destitute widow)
    p1 = add_person(
        client,
        family_id,
        name="Grandmother",
        age=68,
        gender="female",
        marital_status="widowed",
        special_flags=["destitute"],
    )

    # Member 2: College student daughter (age 19, student, higher_secondary)
    p2 = add_person(
        client,
        family_id,
        name="Daughter",
        age=19,
        gender="female",
        education_level="higher_secondary",
        occupation="student",
        marital_status="single",
    )

    res = client.get(f"/families/{family_id}/eligibility")
    assert res.status_code == status.HTTP_200_OK
    fam_data = res.json()
    assert fam_data["family_id"] == family_id
    assert fam_data["total_persons"] == 2
    assert len(fam_data["persons_eligibility"]) == 2

    # Check grandmother's results
    gm_res = next(p for p in fam_data["persons_eligibility"] if p["person_id"] == p1)
    gm_codes = [s["scheme_code"] for s in gm_res["eligible_schemes"]]
    assert "TN-SW-OAP" in gm_codes
    assert "TN-SW-DWP" in gm_codes

    # Check daughter's results (eligible for Pudhumai Penn)
    daughter_res = next(p for p in fam_data["persons_eligibility"] if p["person_id"] == p2)
    daughter_codes = [s["scheme_code"] for s in daughter_res["eligible_schemes"]]
    assert "TN-SW-PUDHUMAI-PENN" in daughter_codes


def test_eligibility_endpoints_404_for_nonexistent_ids(client):
    fake_id = str(uuid.uuid4())
    res_p = client.get(f"/persons/{fake_id}/eligibility")
    assert res_p.status_code == status.HTTP_404_NOT_FOUND

    res_f = client.get(f"/families/{fake_id}/eligibility")
    assert res_f.status_code == status.HTTP_404_NOT_FOUND


def test_matching_engine_is_strictly_deterministic(client):
    """The engine must produce identical results across multiple invocations."""
    family_id = create_family(client, income=4500.00)
    person_id = add_person(
        client,
        family_id,
        name="Chitra",
        age=24,
        gender="female",
        marital_status="single",
        special_flags=["orphan"],
    )

    res1 = client.get(f"/persons/{person_id}/eligibility").json()
    res2 = client.get(f"/persons/{person_id}/eligibility").json()
    res3 = client.get(f"/persons/{person_id}/eligibility").json()

    assert res1 == res2 == res3
    # Orphan girl marriage scheme should be matched
    codes = [s["scheme_code"] for s in res1["eligible_schemes"]]
    assert "TN-SW-ORPHAN-GIRL-MARRIAGE" in codes
