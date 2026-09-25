import uuid
from fastapi import status
from app.models.person import Person
from app.models.family import Family
from app.models.scheme import Scheme, EligibilityRule, SchemeTermGlossary


def test_list_all_schemes(client):
    response = client.get("/schemes")
    assert response.status_code == status.HTTP_200_OK
    schemes = response.json()
    assert len(schemes) >= 15  # We seeded 16 verified schemes
    codes = [s["scheme_code"] for s in schemes]
    assert "TN-SW-OAP" in codes
    assert "TN-SW-DWP" in codes
    assert "TN-SW-KMUT" in codes
    assert "TN-SW-PUDHUMAI-PENN" in codes
    assert "TN-SW-SEWING-MACHINE" in codes
    assert "TN-SW-WIDOW-REMARRIAGE" in codes
    assert "TN-SW-DA-MOTOR-VEHICLE" in codes


def test_filter_schemes_by_department(client):
    # Filter by Differently Abled Welfare
    res_da = client.get("/schemes?department=Differently Abled")
    assert res_da.status_code == status.HTTP_200_OK
    da_schemes = res_da.json()
    assert len(da_schemes) >= 3
    for s in da_schemes:
        assert "Differently Abled" in s["department"]

    # Filter by Social Welfare & Women Empowerment
    res_sw = client.get("/schemes?department=Social Welfare")
    assert res_sw.status_code == status.HTTP_200_OK
    sw_schemes = res_sw.json()
    assert len(sw_schemes) >= 10
    for s in sw_schemes:
        assert "Social Welfare" in s["department"]


def test_filter_schemes_by_category(client):
    # Filter by pension
    res_pension = client.get("/schemes?category=pension")
    assert res_pension.status_code == status.HTTP_200_OK
    pension_schemes = res_pension.json()
    assert len(pension_schemes) >= 4
    for s in pension_schemes:
        assert s["category"] == "pension"

    # Filter by marriage_assistance
    res_marriage = client.get("/schemes?category=marriage_assistance")
    assert res_marriage.status_code == status.HTTP_200_OK
    marriage_schemes = res_marriage.json()
    assert len(marriage_schemes) >= 4
    for s in marriage_schemes:
        assert s["category"] == "marriage_assistance"


def test_get_scheme_by_code_and_by_uuid_with_rules(client):
    # Fetch by code
    res = client.get("/schemes/TN-SW-OAP")
    assert res.status_code == status.HTTP_200_OK
    data = res.json()
    assert data["scheme_code"] == "TN-SW-OAP"
    assert "rules" in data
    assert len(data["rules"]) == 3

    # Check rule details
    rule_fields = [r["field_name"] for r in data["rules"]]
    assert "age" in rule_fields
    assert "special_flags" in rule_fields
    assert "total_household_income" in rule_fields

    # Fetch by UUID
    scheme_uuid = data["id"]
    res_uuid = client.get(f"/schemes/{scheme_uuid}")
    assert res_uuid.status_code == status.HTTP_200_OK
    assert res_uuid.json()["scheme_code"] == "TN-SW-OAP"


def test_get_scheme_not_found(client):
    # Random code
    res_code = client.get("/schemes/NON-EXISTENT-SCHEME")
    assert res_code.status_code == status.HTTP_404_NOT_FOUND

    # Random UUID
    fake_uuid = str(uuid.uuid4())
    res_uuid = client.get(f"/schemes/{fake_uuid}")
    assert res_uuid.status_code == status.HTTP_404_NOT_FOUND


def test_get_glossary_and_search(client):
    res = client.get("/glossary")
    assert res.status_code == status.HTTP_200_OK
    terms = res.json()
    assert len(terms) >= 15

    # Test search for Tamil term "விதவை"
    res_search = client.get("/glossary?search=விதவை")
    assert res_search.status_code == status.HTTP_200_OK
    filtered = res_search.json()
    assert len(filtered) >= 1
    assert any("விதவை" in t["tamil_term"] for t in filtered)

    # Test search for English term "Priority"
    res_search_en = client.get("/glossary?search=Priority")
    assert res_search_en.status_code == status.HTTP_200_OK
    filtered_en = res_search_en.json()
    assert len(filtered_en) >= 1


def test_all_eligibility_rules_reference_valid_models(db_session):
    """Integrity check: Every rule's field_name must match a valid Person or Family attribute."""
    person_columns = {c.name for c in Person.__table__.columns}
    family_columns = {c.name for c in Family.__table__.columns}

    rules = db_session.query(EligibilityRule).all()
    assert len(rules) > 0

    for rule in rules:
        if rule.applies_to.value == "person":
            assert rule.field_name in person_columns, (
                f"Rule {rule.id} references invalid Person field: '{rule.field_name}'"
            )
        elif rule.applies_to.value == "family":
            assert rule.field_name in family_columns, (
                f"Rule {rule.id} references invalid Family field: '{rule.field_name}'"
            )


def test_all_schemes_have_verified_official_sources(db_session):
    """Integrity check: Every scheme must have official source URL and verification date."""
    schemes = db_session.query(Scheme).all()
    assert len(schemes) >= 15

    for scheme in schemes:
        assert scheme.source_url.startswith("http"), (
            f"Scheme {scheme.scheme_code} has invalid source URL: {scheme.source_url}"
        )
        assert scheme.last_verified_date is not None, (
            f"Scheme {scheme.scheme_code} is missing last_verified_date"
        )
        assert scheme.benefit_amount and len(scheme.benefit_amount.strip()) > 0
        assert scheme.name_tamil and len(scheme.name_tamil.strip()) > 0
        assert scheme.name_english and len(scheme.name_english.strip()) > 0
