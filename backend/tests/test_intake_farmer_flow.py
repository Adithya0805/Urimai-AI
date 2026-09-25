import uuid
from decimal import Decimal
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.models.person import Person


def test_intake_farmer_adaptive_flow(client: TestClient, db_session: Session):
    """Test that answering 'விவசாயி' (farmer) triggers agriculture-specific follow-ups:
    1. Land holding in acres
    2. Primary crop type
    and persists these fields into the Person database record.
    """
    session_id = f"farmer-test-{uuid.uuid4()}"

    def send(msg: str):
        res = client.post("/intake/message", json={"session_id": session_id, "message": msg})
        assert res.status_code == 200
        return res.json()

    # Step 1: Start
    r = send("வணக்கம்")
    assert "குடும்ப அமைப்பை குறிப்பிடவும்" in r["reply"]

    # Step 2: Family composition
    r = send("தனி நபர்")
    assert "மாவட்டம்" in r["reply"]

    # Step 3: District
    r = send("தஞ்சாவூர்")
    assert "வட்டம்" in r["reply"]

    # Step 4: Taluk
    r = send("கும்பகோணம்")
    assert "முகவரி" in r["reply"]

    # Step 5: Address
    r = send("15, மேல வீதி")
    assert "குடும்ப அட்டை" in r["reply"]

    # Step 6: Ration Card
    r = send("பச்சை அட்டை")
    assert "வருமானம்" in r["reply"]

    # Step 7: Income
    r = send("8000")
    assert "நபர்களின்" in r["reply"]

    # Step 8: Person Count
    r = send("1 நபர்")
    assert "முழு பெயர்" in r["reply"]

    # Step 9: Person 1 Name
    r = send("செல்வராஜ்")
    assert "வயது என்ன" in r["reply"]

    # Step 10: Age
    r = send("48")
    assert "பாலினம்" in r["reply"]

    # Step 11: Gender
    r = send("ஆண்")
    assert "கல்வித் தகுதி" in r["reply"]

    # Step 12: Education
    r = send("தொடக்கக் கல்வி")
    assert "தொழில் என்ன" in r["reply"]

    # Step 13: Occupation -> Farmer!
    r = send("விவசாயி")
    # Must ask land holding follow-up
    assert r["current_step"] == "person_land_holding"
    assert "நிலத்தின் அளவு" in r["reply"]

    # Step 14: Land holding -> 2.5 acres
    r = send("2.5 ஏக்கர்")
    # Must ask crop type follow-up
    assert r["current_step"] == "person_crop_type"
    assert "பயிரிடப்படும் முதன்மைப் பயிர்" in r["reply"]

    # Step 15: Crop type -> Paddy
    r = send("நெல்")
    # Must now proceed to marital status
    assert r["current_step"] == "person_marital"
    assert "திருமண நிலை" in r["reply"]

    # Step 16: Marital status
    r = send("திருமணமானவர்")
    assert "சமூகப் பிரிவு" in r["reply"]

    # Step 17: Caste Category
    r = send("BC")
    assert "மாற்றுத்திறனாளி" in r["reply"]

    # Step 18: Disability
    r = send("இல்லை")
    assert "சிறப்பு" in r["reply"]

    # Step 19: Special Flags
    r = send("எதுவுமில்லை")
    # Reaches summary
    assert r["current_step"] == "confirm_summary"
    assert "2.5" in r["reply"]
    assert "paddy" in r["reply"]

    # Step 20: Confirm and save
    r = send("ஆம், சரியானவை")
    assert r["is_completed"] is True
    assert "வெற்றிகரமாக பதிவு" in r["reply"]

    # Verify database persistence of agriculture fields
    saved_person_id = r["saved_person_ids"][0]
    db_person = db_session.query(Person).filter(Person.id == uuid.UUID(saved_person_id)).first()
    assert db_person is not None
    assert db_person.occupation.value == "farmer"
    assert float(db_person.land_holding_acres) == 2.5
    assert db_person.crop_type == "paddy"


def test_intake_non_farmer_skips_agriculture_questions(client: TestClient):
    """Test that answering a non-farmer occupation (e.g. 'தினக்கூலி' or 'மாணவர்')
    skips land holding and crop type questions directly to marital status.
    """
    session_id = f"non-farmer-test-{uuid.uuid4()}"

    def send(msg: str):
        res = client.post("/intake/message", json={"session_id": session_id, "message": msg})
        assert res.status_code == 200
        return res.json()

    send("வணக்கம்")
    send("தனி நபர்")
    send("மதுரை")
    send("மதுரை வடக்கு")
    send("10 தெற்கு வீதி")
    send("பச்சை அட்டை")
    send("5000")
    send("1 நபர்")
    send("முருகன்")
    send("35")
    send("ஆண்")
    send("பத்தாம் வகுப்பு")

    # Enter non-farmer occupation
    r = send("தினக்கூலி")
    # Must skip land holding and go directly to marital status
    assert r["current_step"] == "person_marital"
    assert "திருமண நிலை" in r["reply"]
