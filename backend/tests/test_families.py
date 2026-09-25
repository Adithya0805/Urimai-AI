import uuid
from fastapi import status


def test_create_family_success(client):
    payload = {
        "composition_type": "nuclear",
        "district": "Madurai",
        "taluk": "Madurai North",
        "address": "12, Periyar Nagar, Sellur",
        "ration_card_type": "green",
        "total_household_income": 18500.50,
    }
    response = client.post("/families", json=payload)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert "id" in data
    assert data["composition_type"] == "nuclear"
    assert data["district"] == "Madurai"
    assert data["taluk"] == "Madurai North"
    assert data["ration_card_type"] == "green"
    assert float(data["total_household_income"]) == 18500.50
    assert "created_at" in data
    assert "updated_at" in data


def test_get_family_by_id(client):
    create_res = client.post(
        "/families",
        json={
            "composition_type": "single",
            "district": "Chennai",
            "taluk": "Mylapore",
            "address": "45, Luz Church Road",
            "ration_card_type": "white",
            "total_household_income": 12000.00,
        },
    )
    family_id = create_res.json()["id"]

    get_res = client.get(f"/families/{family_id}")
    assert get_res.status_code == status.HTTP_200_OK
    data = get_res.json()
    assert data["id"] == family_id
    assert data["district"] == "Chennai"
    assert data["persons"] == []


def test_get_nonexistent_family_returns_404(client):
    fake_id = str(uuid.uuid4())
    response = client.get(f"/families/{fake_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert f"Family with id '{fake_id}' not found" in response.json()["detail"]


def test_patch_family(client):
    create_res = client.post(
        "/families",
        json={
            "composition_type": "couple",
            "district": "Coimbatore",
            "taluk": "Pollachi",
            "address": "7, Gandhi Salai",
            "ration_card_type": "green",
            "total_household_income": 20000.00,
        },
    )
    family_id = create_res.json()["id"]

    patch_res = client.patch(
        f"/families/{family_id}",
        json={
            "address": "7A, Gandhi Salai (Renovated)",
            "total_household_income": 25000.00,
            "composition_type": "nuclear",
        },
    )
    assert patch_res.status_code == status.HTTP_200_OK
    updated_data = patch_res.json()
    assert updated_data["address"] == "7A, Gandhi Salai (Renovated)"
    assert float(updated_data["total_household_income"]) == 25000.00
    assert updated_data["composition_type"] == "nuclear"
    assert updated_data["district"] == "Coimbatore"  # Unmodified field preserved


def test_patch_nonexistent_family_returns_404(client):
    fake_id = str(uuid.uuid4())
    response = client.patch(f"/families/{fake_id}", json={"district": "Salem"})
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_reject_invalid_composition_enum(client):
    payload = {
        "composition_type": "unextended_tribe",  # Invalid enum value
        "district": "Tiruchirappalli",
        "taluk": "Srirangam",
        "address": "5, South Street",
        "ration_card_type": "green",
        "total_household_income": 15000,
    }
    response = client.post("/families", json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_reject_invalid_ration_card_enum(client):
    payload = {
        "composition_type": "nuclear",
        "district": "Tiruchirappalli",
        "taluk": "Srirangam",
        "address": "5, South Street",
        "ration_card_type": "purple",  # Invalid ration card type
        "total_household_income": 15000,
    }
    response = client.post("/families", json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_reject_negative_income(client):
    payload = {
        "composition_type": "nuclear",
        "district": "Tiruchirappalli",
        "taluk": "Srirangam",
        "address": "5, South Street",
        "ration_card_type": "green",
        "total_household_income": -500.00,  # Negative income disallowed
    }
    response = client.post("/families", json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
