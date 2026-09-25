import uuid
from decimal import Decimal
from fastapi.testclient import TestClient

from app.models.enums import ApplicationMode


def create_family(
    client: TestClient,
    income=0,
    district="Madurai",
    taluk="Madurai North",
    composition="nuclear",
    ration_card="green",
):
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
    assert res.status_code == 201
    return res.json()["id"]


def add_person(client: TestClient, family_id: str, **kwargs):
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
    assert res.status_code == 201
    return res.json()["id"]


def test_eligible_person_guidance_complete_plan(client: TestClient):
    """Test that an eligible senior destitute widow receives a complete step-by-step
    guidance package in Tamil for Old Age Pension (OAP), with verified official documents and offices.
    """
    family_id = create_family(client, income=4000, composition="single")
    person_id = add_person(
        client,
        family_id,
        name="மீனாட்சி அம்மாள்",
        age=65,
        gender="female",
        education_level="none",
        occupation="unemployed",
        marital_status="widowed",
        caste_category="BC",
        disability_status=False,
        special_flags=["destitute"],
    )

    response = client.get(f"/persons/{person_id}/guidance")
    assert response.status_code == 200
    data = response.json()

    assert data["person_id"] == person_id
    assert data["person_name"] == "மீனாட்சி அம்மாள்"
    assert data["eligible_schemes_count"] >= 1

    # Verify TN-SW-OAP is in eligible schemes guidance
    oap_guidance = next(
        (g for g in data["eligible_schemes_guidance"] if g["scheme_code"] == "TN-SW-OAP"),
        None,
    )
    assert oap_guidance is not None
    assert oap_guidance["name_english"] == "Indira Gandhi National Old Age Pension Scheme / State Old Age Pension"
    assert "ஓய்வூதியம்" in oap_guidance["name_tamil"]
    assert oap_guidance["benefit_amount"] == "₹1,000/month"
    assert len(oap_guidance["required_documents"]) >= 3
    assert any("ஆதார்" in doc for doc in oap_guidance["required_documents"])
    assert "வட்டாட்சியர்" in oap_guidance["where_to_apply_tamil"]
    assert oap_guidance["application_mode"] == ApplicationMode.BOTH.value
    assert len(oap_guidance["steps_tamil"]) == 4
    assert oap_guidance["steps_tamil"][0].startswith("1. தேவையான ஆவணங்களை")
    assert oap_guidance["steps_tamil"][2].startswith("3. விண்ணப்பத்தை")
    assert oap_guidance["processing_time_estimate"] == "30 நாட்கள்"
    assert oap_guidance["is_stale"] is False
    assert oap_guidance["disclaimer_tamil"] is None


def test_partially_eligible_person_guidance_gap_analysis(client: TestClient):
    """Test that a 45-year-old destitute widow receives clear Tamil gap guidance
    explaining that age 60 is required, and actionable advice on when/how to qualify.
    """
    family_id = create_family(client, income=3500, composition="single")
    person_id = add_person(
        client,
        family_id,
        name="காளியம்மாள்",
        age=45,
        gender="female",
        education_level="primary",
        occupation="daily_wage",
        marital_status="widowed",
        caste_category="MBC",
        disability_status=False,
        special_flags=["destitute"],
    )

    response = client.get(f"/persons/{person_id}/guidance")
    assert response.status_code == 200
    data = response.json()

    assert data["partially_eligible_schemes_count"] >= 1
    oap_partial = next(
        (g for g in data["partially_eligible_schemes_guidance"] if g["scheme_code"] == "TN-SW-OAP"),
        None,
    )
    assert oap_partial is not None
    # Check that age failure is translated accurately to Tamil
    missing_text = " ".join(oap_partial["missing_conditions_tamil"])
    assert "வயது 45" in missing_text
    assert "60" in missing_text

    # Check actionable resolution in Tamil
    resolution_text = " ".join(oap_partial["how_to_resolve_tamil"])
    assert "60 வயது" in resolution_text


def test_guidance_staleness_disclaimer_triggered(client: TestClient):
    """Test that a scheme with last_verified_date > 180 days ago (TN-SW-GIRL-CHILD-1)
    triggers is_stale=True and displays the official staleness disclaimer in Tamil.
    """
    family_id = create_family(client, income=5000, composition="nuclear")
    # Female child aged 2 is eligible for TN-SW-GIRL-CHILD-1
    person_id = add_person(
        client,
        family_id,
        name="அமுதவல்லி",
        age=2,
        gender="female",
        education_level="none",
        occupation="student",
        marital_status="single",
        caste_category="MBC",
        disability_status=False,
        special_flags=[],
    )

    response = client.get(f"/persons/{person_id}/guidance")
    assert response.status_code == 200
    data = response.json()

    # Look for TN-SW-GIRL-CHILD-1 in eligible schemes
    girl_child_guidance = next(
        (g for g in data["eligible_schemes_guidance"] if g["scheme_code"] == "TN-SW-GIRL-CHILD-1"),
        None,
    )
    assert girl_child_guidance is not None
    assert girl_child_guidance["is_stale"] is True
    assert girl_child_guidance["disclaimer_tamil"] is not None
    assert "6 மாதங்களுக்கு மேல்" in girl_child_guidance["disclaimer_tamil"]


def test_guidance_application_mode_variations(client: TestClient):
    """Test that online, offline, and both application modes render correctly formatted
    Tamil instructions and office locations.
    """
    # 1. Test ONLINE scheme: Pudhumai Penn (TN-SW-PUDHUMAI-PENN)
    family_id = create_family(client, income=15000, composition="nuclear")
    student_id = add_person(
        client,
        family_id,
        name="கவிதா",
        age=19,
        gender="female",
        education_level="graduate",
        occupation="student",
        marital_status="single",
        caste_category="BC",
        disability_status=False,
        special_flags=[],
    )

    res_student = client.get(f"/persons/{student_id}/guidance")
    assert res_student.status_code == 200
    pudhumai_guidance = next(
        (g for g in res_student.json()["eligible_schemes_guidance"] if g["scheme_code"] == "TN-SW-PUDHUMAI-PENN"),
        None,
    )
    assert pudhumai_guidance is not None
    assert pudhumai_guidance["application_mode"] == ApplicationMode.ONLINE.value
    assert "இணையதளம் வழியாக மட்டுமே" in pudhumai_guidance["where_to_apply_tamil"]
    assert "pudhumaipenn.tn.gov.in" in pudhumai_guidance["online_application_url"]
    assert "இணையதளத்திற்குச் சென்று" in pudhumai_guidance["steps_tamil"][1]

    # 2. Test OFFLINE scheme: Girl Child Protection Scheme (TN-SW-GIRL-CHILD-1)
    child_id = add_person(
        client,
        family_id,
        name="பாப்பா",
        age=1,
        gender="female",
        education_level="none",
        occupation="student",
        marital_status="single",
        caste_category="BC",
        disability_status=False,
        special_flags=[],
    )
    # Give low income so eligible
    client.patch(f"/families/{family_id}", json={"total_household_income": 4000})
    res_child = client.get(f"/persons/{child_id}/guidance")
    assert res_child.status_code == 200
    girl_guidance = next(
        (g for g in res_child.json()["eligible_schemes_guidance"] if g["scheme_code"] == "TN-SW-GIRL-CHILD-1"),
        None,
    )
    assert girl_guidance is not None
    assert girl_guidance["application_mode"] == ApplicationMode.OFFLINE.value
    assert "நேரடியாக விண்ணப்பிக்க வேண்டிய அலுவலகம்" in girl_guidance["where_to_apply_tamil"]
    assert "நேரில் சென்று" in girl_guidance["steps_tamil"][1]


def test_family_guidance_endpoint(client: TestClient):
    """Test that GET /families/{family_id}/guidance returns full guidance packages
    for every family member.
    """
    family_id = create_family(client, income=8000, composition="nuclear")
    add_person(
        client,
        family_id,
        name="கண்ணன்",
        age=68,
        gender="male",
        education_level="primary",
        occupation="retired",
        marital_status="married",
        caste_category="BC",
        disability_status=False,
        special_flags=["destitute"],
    )
    add_person(
        client,
        family_id,
        name="லட்சுமி",
        age=63,
        gender="female",
        education_level="none",
        occupation="homemaker",
        marital_status="married",
        caste_category="BC",
        disability_status=False,
        special_flags=["destitute"],
    )

    response = client.get(f"/families/{family_id}/guidance")
    assert response.status_code == 200
    data = response.json()

    assert data["family_id"] == family_id
    assert data["total_persons"] == 2
    assert len(data["persons_guidance"]) == 2
    names = [p["person_name"] for p in data["persons_guidance"]]
    assert "கண்ணன்" in names
    assert "லட்சுமி" in names


def test_guidance_404_not_found(client: TestClient):
    """Test that requesting guidance for non-existent IDs returns HTTP 404."""
    random_id = uuid.uuid4()
    res_person = client.get(f"/persons/{random_id}/guidance")
    assert res_person.status_code == 404
    assert "not found" in res_person.json()["detail"].lower()

    res_family = client.get(f"/families/{random_id}/guidance")
    assert res_family.status_code == 404
    assert "not found" in res_family.json()["detail"].lower()
