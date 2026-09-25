from typing import TypedDict, List, Dict, Any, Optional


class IntakeState(TypedDict):
    session_id: str
    current_step: str
    family_data: Dict[str, Any]
    persons_data: List[Dict[str, Any]]
    total_persons_target: int
    current_person_idx: int
    current_person_temp: Dict[str, Any]
    latest_user_message: str
    reply: str
    pending_clarification: Optional[str]
    last_question: str
    summary_tamil: Optional[str]
    is_confirmed: bool
    is_completed: bool
    saved_family_id: Optional[str]
    saved_person_ids: List[str]
    extraction_log: List[Dict[str, Any]]


def create_initial_state(session_id: str) -> IntakeState:
    return {
        "session_id": session_id,
        "current_step": "greet",
        "family_data": {},
        "persons_data": [],
        "total_persons_target": 1,
        "current_person_idx": 0,
        "current_person_temp": {},
        "latest_user_message": "",
        "reply": "",
        "pending_clarification": None,
        "last_question": "",
        "summary_tamil": None,
        "is_confirmed": False,
        "is_completed": False,
        "saved_family_id": None,
        "saved_person_ids": [],
        "extraction_log": [],
    }
