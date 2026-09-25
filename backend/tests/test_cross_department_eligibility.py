import uuid
from decimal import Decimal
from fastapi.testclient import TestClient


def create_family(
    client: TestClient,
    income=0,
    district="Thanjavur",
    taluk="Kumbakonam",
    composition="nuclear",
    ration_card="green",
):
    res = client.post(
        "/families",
        json={
            "composition_type": composition,
            "district": district,
            "taluk": taluk,
            "address": "24, Sannadhi Street",
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
        "land_holding_acres": 0.0,
        "crop_type": None,
    }
    default_payload.update(kwargs)
    res = client.post(f"/families/{family_id}/persons", json=default_payload)
    assert res.status_code == 201
    return res.json()["id"]


def test_farmer_family_cross_department_matching_agriculture_and_education(client: TestClient):
    """Profile: A delta farming family in Thanjavur.
    - Father is a paddy farmer holding 2.5 acres.
    - Son is a college undergraduate student (BC).
    - Daughter is a 12th standard student (BC).

    Test verifies:
    1. Father matches multiple Agriculture schemes (PM-KISAN, Kuruvai Package, Micro-Irrigation).
    2. Son matches Education schemes (Tamil Pudhalvan, BC Free Degree, BC Post-Matric).
    3. Daughter matches Education schemes (Free Laptop, Free Bicycle, Periyar Award).
    4. Family eligibility endpoint returns cross-department schemes concurrently.
    """
    family_id = create_family(client, income=8000, district="Thanjavur", taluk="Papanasam")

    # 1. Father - Paddy Farmer
    father_id = add_person(
        client,
        family_id,
        name="செல்வராஜ்",
        age=48,
        gender="male",
        education_level="primary",
        occupation="farmer",
        marital_status="married",
        caste_category="BC",
        disability_status=False,
        special_flags=[],
        land_holding_acres=2.5,
        crop_type="paddy",
    )

    # 2. Son - College Student (Tamil Pudhalvan & BC Scholarship eligible)
    son_id = add_person(
        client,
        family_id,
        name="கார்த்திக்",
        age=19,
        gender="male",
        education_level="graduate",
        occupation="student",
        marital_status="single",
        caste_category="BC",
        disability_status=False,
        special_flags=[],
    )

    # 3. Daughter - 12th Std School Student
    daughter_id = add_person(
        client,
        family_id,
        name="காவியா",
        age=17,
        gender="female",
        education_level="higher_secondary",
        occupation="student",
        marital_status="single",
        caste_category="BC",
        disability_status=False,
        special_flags=[],
    )

    # Fetch family eligibility
    res_fam = client.get(f"/families/{family_id}/eligibility")
    assert res_fam.status_code == 200
    data = res_fam.json()

    assert data["total_persons"] == 3

    # Check Father matches Agriculture schemes
    father_eval = next(p for p in data["persons_eligibility"] if p["person_id"] == father_id)
    agri_codes = [s["scheme_code"] for s in father_eval["eligible_schemes"]]
    assert "TN-AGRI-PM-KISAN" in agri_codes
    assert "TN-AGRI-KURUVAI-PACKAGE" in agri_codes
    assert "TN-AGRI-MICRO-IRRIGATION-MIF" in agri_codes
    assert "TN-AGRI-CROP-INSURANCE-PMFBY" in agri_codes

    # Check Son matches Education schemes
    son_eval = next(p for p in data["persons_eligibility"] if p["person_id"] == son_id)
    son_codes = [s["scheme_code"] for s in son_eval["eligible_schemes"]]
    assert "TN-EDU-TAMIL-PUDHALVAN" in son_codes
    assert "TN-EDU-POST-MATRIC-BC-MBC" in son_codes
    assert "TN-EDU-FREE-EDUCATION-BC-DEGREE" in son_codes

    # Check Daughter matches Education schemes
    daughter_eval = next(p for p in data["persons_eligibility"] if p["person_id"] == daughter_id)
    daughter_codes = [s["scheme_code"] for s in daughter_eval["eligible_schemes"]]
    assert "TN-EDU-FREE-LAPTOP" in daughter_codes
    assert "TN-EDU-FREE-BICYCLE" in daughter_codes
    assert "TN-EDU-PERIYAR-AWARD-GIRL-STUDENTS" in daughter_codes

    # Check Guidance generation works across departments
    res_guidance = client.get(f"/families/{family_id}/guidance")
    assert res_guidance.status_code == 200
    guidance_data = res_guidance.json()
    assert len(guidance_data["persons_guidance"]) == 3


def test_individual_cross_matching_social_welfare_and_agriculture(client: TestClient):
    """Profile: A 65-year-old destitute farmer with 1 acre dry land and monthly income ₹4,000.
    Should match BOTH:
    1. Social Welfare: TN-SW-OAP (Old Age Pension)
    2. Agriculture: TN-AGRI-UZHAVAR-PATHUKAPPU-PENSION and TN-AGRI-PM-KISAN
    """
    family_id = create_family(client, income=4000, composition="single")
    person_id = add_person(
        client,
        family_id,
        name="முத்துசாமி",
        age=65,
        gender="male",
        education_level="none",
        occupation="farmer",
        marital_status="widowed",
        caste_category="BC",
        disability_status=False,
        special_flags=["destitute"],
        land_holding_acres=1.0,
        crop_type="millets",
    )

    res = client.get(f"/persons/{person_id}/eligibility")
    assert res.status_code == 200
    data = res.json()

    eligible_codes = [s["scheme_code"] for s in data["eligible_schemes"]]
    departments = {s["department"] for s in data["eligible_schemes"]}

    # Matches across departments simultaneously for the same person
    assert "Social Welfare & Women Empowerment" in departments
    assert "Agriculture and Farmers Welfare" in departments
    assert "TN-SW-OAP" in eligible_codes
    assert "TN-AGRI-UZHAVAR-PATHUKAPPU-PENSION" in eligible_codes
    assert "TN-AGRI-PM-KISAN" in eligible_codes
    assert "TN-AGRI-MILLETS-MISSION" in eligible_codes


def test_construction_worker_matching_labour_department(client: TestClient):
    """Profile: A registered female construction worker in Chennai, age 26, married.
    Matches:
    - TN-LAB-CONSTRUCTION-BOARD-ACCIDENT-RELIEF
    - TN-LAB-CONSTRUCTION-BOARD-MATERNITY
    - TN-LAB-CONSTRUCTION-BOARD-MARRIAGE-ASSISTANCE
    """
    family_id = create_family(client, income=9000, composition="nuclear", district="Chennai")
    worker_id = add_person(
        client,
        family_id,
        name="மலர்விழி",
        age=26,
        gender="female",
        education_level="secondary",
        occupation="daily_wage",
        marital_status="married",
        caste_category="SC",
        disability_status=False,
        special_flags=["registered_construction_worker"],
    )

    res = client.get(f"/persons/{worker_id}/eligibility")
    assert res.status_code == 200
    data = res.json()

    eligible_codes = [s["scheme_code"] for s in data["eligible_schemes"]]
    assert "TN-LAB-CONSTRUCTION-BOARD-ACCIDENT-RELIEF" in eligible_codes
    assert "TN-LAB-CONSTRUCTION-BOARD-MATERNITY" in eligible_codes
    assert "TN-LAB-CONSTRUCTION-BOARD-MARRIAGE-ASSISTANCE" in eligible_codes


def test_unemployed_graduate_job_seeker_matching(client: TestClient):
    """Profile: 23-year-old unemployed graduate job seeker.
    Matches:
    - TN-LAB-UNEMPLOYMENT-ASSISTANCE-GRADUATE
    - TN-LAB-SKILL-TRAINING-TNSDC (Naan Mudhalvan skill training)
    """
    family_id = create_family(client, income=12000, composition="nuclear", district="Salem")
    person_id = add_person(
        client,
        family_id,
        name="சரவணன்",
        age=23,
        gender="male",
        education_level="graduate",
        occupation="unemployed",
        marital_status="single",
        caste_category="MBC",
        disability_status=False,
        special_flags=[],
    )

    res = client.get(f"/persons/{person_id}/eligibility")
    assert res.status_code == 200
    data = res.json()

    eligible_codes = [s["scheme_code"] for s in data["eligible_schemes"]]
    assert "TN-LAB-UNEMPLOYMENT-ASSISTANCE-GRADUATE" in eligible_codes
    assert "TN-LAB-SKILL-TRAINING-TNSDC" in eligible_codes
