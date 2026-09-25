import uuid
from fastapi import status


def create_sample_family(client):
    res = client.post(
        "/families",
        json={
            "composition_type": "joint",
            "district": "Thanjavur",
            "taluk": "Kumbakonam",
            "address": "24, Big Bazaar Street",
            "ration_card_type": "green",
            "total_household_income": 22000.00,
        },
    )
    assert res.status_code == status.HTTP_201_CREATED
    return res.json()["id"]


def test_add_person_to_family_success(client):
    family_id = create_sample_family(client)

    person_payload = {
        "name": "Selvi Murugan",
        "age": 34,
        "gender": "female",
        "education_level": "higher_secondary",
        "occupation": "self_employed",
        "occupation_detail": "Tailoring shop",
        "marital_status": "married",
        "caste_category": "BC",
        "disability_status": False,
        "disability_type": None,
        "special_flags": ["folk_artist"],
    }
    response = client.post(f"/families/{family_id}/persons", json=person_payload)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert "id" in data
    assert data["family_id"] == family_id
    assert data["name"] == "Selvi Murugan"
    assert data["age"] == 34
    assert data["gender"] == "female"
    assert data["education_level"] == "higher_secondary"
    assert data["occupation"] == "self_employed"
    assert data["occupation_detail"] == "Tailoring shop"
    assert data["marital_status"] == "married"
    assert data["caste_category"] == "BC"
    assert data["disability_status"] is False
    assert data["special_flags"] == ["folk_artist"]


def test_add_multiple_persons_and_fetch_full_family_list(client):
    family_id = create_sample_family(client)

    persons_to_add = [
        {
            "name": "Arun Kumar",
            "age": 42,
            "gender": "male",
            "education_level": "graduate",
            "occupation": "farmer",
            "marital_status": "married",
            "caste_category": "MBC",
            "disability_status": False,
            "special_flags": [],
        },
        {
            "name": "Kavitha Arun",
            "age": 38,
            "gender": "female",
            "education_level": "secondary",
            "occupation": "homemaker",
            "marital_status": "married",
            "caste_category": "MBC",
            "disability_status": False,
            "special_flags": [],
        },
        {
            "name": "Mithun Arun",
            "age": 14,
            "gender": "male",
            "education_level": "secondary",
            "occupation": "student",
            "marital_status": "single",
            "caste_category": "MBC",
            "disability_status": False,
            "special_flags": [],
        },
    ]

    added_ids = []
    for p in persons_to_add:
        res = client.post(f"/families/{family_id}/persons", json=p)
        assert res.status_code == status.HTTP_201_CREATED
        added_ids.append(res.json()["id"])

    # 1. Fetch via GET /families/{id}/persons
    list_res = client.get(f"/families/{family_id}/persons")
    assert list_res.status_code == status.HTTP_200_OK
    person_list = list_res.json()
    assert len(person_list) == 3
    retrieved_names = [p["name"] for p in person_list]
    assert "Arun Kumar" in retrieved_names
    assert "Kavitha Arun" in retrieved_names
    assert "Mithun Arun" in retrieved_names

    # 2. Fetch via GET /families/{id} with embedded persons
    family_res = client.get(f"/families/{family_id}")
    assert family_res.status_code == status.HTTP_200_OK
    family_data = family_res.json()
    assert len(family_data["persons"]) == 3


def test_update_person_occupation(client):
    family_id = create_sample_family(client)

    # Add person
    add_res = client.post(
        f"/families/{family_id}/persons",
        json={
            "name": "Vetrivel",
            "age": 28,
            "gender": "male",
            "education_level": "graduate",
            "occupation": "unemployed",
            "marital_status": "single",
            "caste_category": "SC",
            "disability_status": False,
            "special_flags": [],
        },
    )
    person_id = add_res.json()["id"]

    # Patch occupation to govt_employee
    patch_res = client.patch(
        f"/persons/{person_id}",
        json={
            "occupation": "govt_employee",
            "occupation_detail": "Junior Assistant, Revenue Dept",
        },
    )
    assert patch_res.status_code == status.HTTP_200_OK
    updated = patch_res.json()
    assert updated["occupation"] == "govt_employee"
    assert updated["occupation_detail"] == "Junior Assistant, Revenue Dept"
    assert updated["name"] == "Vetrivel"  # Unaltered field preserved

    # Verify persistent in database
    get_res = client.get(f"/persons/{person_id}")
    assert get_res.status_code == status.HTTP_200_OK
    assert get_res.json()["occupation"] == "govt_employee"


def test_reject_invalid_age(client):
    family_id = create_sample_family(client)

    # Zero age
    res_zero = client.post(
        f"/families/{family_id}/persons",
        json={
            "name": "Baby",
            "age": 0,
            "gender": "female",
            "education_level": "none",
            "occupation": "homemaker",
            "marital_status": "single",
            "caste_category": "General",
        },
    )
    assert res_zero.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    # Negative age
    res_neg = client.post(
        f"/families/{family_id}/persons",
        json={
            "name": "Invalid Person",
            "age": -5,
            "gender": "male",
            "education_level": "none",
            "occupation": "other",
            "marital_status": "single",
            "caste_category": "General",
        },
    )
    assert res_neg.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_reject_invalid_enum_values(client):
    family_id = create_sample_family(client)

    # Invalid gender
    res = client.post(
        f"/families/{family_id}/persons",
        json={
            "name": "Test Person",
            "age": 30,
            "gender": "unknown_gender",
            "education_level": "graduate",
            "occupation": "farmer",
            "marital_status": "single",
            "caste_category": "General",
        },
    )
    assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    # Invalid caste
    res = client.post(
        f"/families/{family_id}/persons",
        json={
            "name": "Test Person",
            "age": 30,
            "gender": "male",
            "education_level": "graduate",
            "occupation": "farmer",
            "marital_status": "single",
            "caste_category": "NonExistentCaste",
        },
    )
    assert res.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_cannot_add_person_to_nonexistent_family(client):
    fake_family_id = str(uuid.uuid4())
    res = client.post(
        f"/families/{fake_family_id}/persons",
        json={
            "name": "Ghost Member",
            "age": 25,
            "gender": "female",
            "education_level": "graduate",
            "occupation": "student",
            "marital_status": "single",
            "caste_category": "General",
        },
    )
    assert res.status_code == status.HTTP_404_NOT_FOUND
    assert f"Family with id '{fake_family_id}' does not exist" in res.json()["detail"]


def test_get_nonexistent_person_returns_404(client):
    fake_person_id = str(uuid.uuid4())
    res = client.get(f"/persons/{fake_person_id}")
    assert res.status_code == status.HTTP_404_NOT_FOUND


def test_patch_nonexistent_person_returns_404(client):
    fake_person_id = str(uuid.uuid4())
    res = client.patch(f"/persons/{fake_person_id}", json={"occupation": "retired"})
    assert res.status_code == status.HTTP_404_NOT_FOUND
