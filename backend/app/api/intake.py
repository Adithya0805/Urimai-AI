import uuid
from typing import Dict, List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.intake_log import IntakeExtractionLog
from app.schemas.intake import (
    IntakeMessageRequest,
    IntakeMessageResponse,
    IntakeExtractionLogResponse,
)
from app.services.intake_state import IntakeState, create_initial_state
from app.services.intake_graph import process_user_turn

from app.core.auth import get_optional_user, get_current_user, AuthUser

from app.core.rate_limiter import rate_limit
from app.core.sanitizer import sanitize_text

router = APIRouter(prefix="/intake", tags=["Conversational Intake Agent (Tamil)"])

# In-memory session store (can also be persisted to Redis or DB)
SESSIONS: Dict[str, IntakeState] = {}
USER_ACTIVE_SESSIONS: Dict[str, str] = {}  # user_id -> session_id


@router.post(
    "/message",
    response_model=IntakeMessageResponse,
    dependencies=[Depends(rate_limit(max_requests=60, window_seconds=60))],
    summary="Send Message to Tamil Intake Agent",
    description="Processes user conversational turn, updates LangGraph state machine, extracts profile attributes, and returns the next question or summary.",
)
def handle_intake_message(
    payload: IntakeMessageRequest,
    current_user: Optional[AuthUser] = Depends(get_optional_user),
    db: Session = Depends(get_db),
):
    """Process a user message in Tamil, update intake state machine, and return response."""
    session_id = payload.session_id or str(uuid.uuid4())
    if session_id not in SESSIONS:
        SESSIONS[session_id] = create_initial_state(session_id)

    state = SESSIONS[session_id]
    if current_user:
        state["user_id"] = current_user.id
        USER_ACTIVE_SESSIONS[str(current_user.id)] = session_id

    sanitized_msg = sanitize_text(payload.message, max_length=2000)
    updated_state = process_user_turn(state, sanitized_msg, db)
    SESSIONS[session_id] = updated_state

    # Clean active session mapping if completed
    if updated_state.get("is_completed") and current_user:
        USER_ACTIVE_SESSIONS.pop(str(current_user.id), None)

    return IntakeMessageResponse(
        session_id=session_id,
        reply=updated_state["reply"],
        current_step=updated_state["current_step"],
        pending_clarification=updated_state.get("pending_clarification"),
        is_completed=updated_state.get("is_completed", False),
        summary=updated_state.get("summary_tamil"),
        saved_family_id=updated_state.get("saved_family_id"),
        saved_person_ids=updated_state.get("saved_person_ids", []),
    )


@router.get("/resume", response_model=IntakeMessageResponse)
def resume_intake(
    current_user: AuthUser = Depends(get_current_user),
):
    """Resume an uncompleted conversational intake session for the authenticated citizen."""
    user_key = str(current_user.id)
    session_id = USER_ACTIVE_SESSIONS.get(user_key)
    if not session_id or session_id not in SESSIONS:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="நிலுவையில் உள்ள பதிவு எதுவும் இல்லை (No active uncompleted intake session found to resume)",
        )

    state = SESSIONS[session_id]
    if state.get("is_completed"):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="பதிவு ஏற்கனவே நிறைவடைந்துவிட்டது (Intake already completed)",
        )

    return IntakeMessageResponse(
        session_id=session_id,
        reply=state["reply"],
        current_step=state["current_step"],
        pending_clarification=state.get("pending_clarification"),
        is_completed=False,
        summary=state.get("summary_tamil"),
        saved_family_id=state.get("saved_family_id"),
        saved_person_ids=state.get("saved_person_ids", []),
    )



@router.get("/state/{session_id}")
def get_intake_state(session_id: str):
    """Retrieve the current state of an intake session."""
    if session_id not in SESSIONS:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Session '{session_id}' not found",
        )
    return SESSIONS[session_id]


@router.get("/logs", response_model=List[IntakeExtractionLogResponse])
def get_extraction_logs(
    session_id: Optional[str] = Query(None, description="Filter logs by session ID"),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    """Retrieve extraction audit logs to review Tamil input parsing accuracy."""
    query = db.query(IntakeExtractionLog)
    if session_id:
        query = query.filter(IntakeExtractionLog.session_id == session_id)
    return query.order_by(IntakeExtractionLog.created_at.desc()).limit(limit).all()


@router.get("/chat", response_class=HTMLResponse)
def get_chat_interface():
    """Serves a clean, mobile-responsive Tamil chat interface for testing intake dialogue."""
    html_content = """<!DOCTYPE html>
<html lang="ta">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>உரிமை AI — உரையாடல் பதிவு (Urimai AI Intake)</title>
    <link href="https://fonts.googleapis.com/css2?family=Mukta+Malar:wght@400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #047857;
            --primary-dark: #065f46;
            --bg: #f8fafc;
            --card: #ffffff;
            --text: #0f172a;
            --text-muted: #64748b;
            --border: #e2e8f0;
            --bot-bubble: #f1f5f9;
            --user-bubble: #047857;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Mukta Malar', 'Inter', sans-serif;
            background: var(--bg);
            color: var(--text);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 1rem;
        }
        .chat-container {
            width: 100%;
            max-width: 650px;
            background: var(--card);
            border-radius: 16px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
            border: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            height: 90vh;
            overflow: hidden;
        }
        .chat-header {
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: white;
            padding: 1.25rem 1.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .header-title h2 { font-size: 1.25rem; font-weight: 700; }
        .header-title p { font-size: 0.85rem; opacity: 0.9; }
        .session-badge {
            background: rgba(255, 255, 255, 0.2);
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-family: monospace;
        }
        .chat-messages {
            flex: 1;
            padding: 1.25rem;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        .message {
            max-width: 82%;
            padding: 0.85rem 1.15rem;
            border-radius: 14px;
            line-height: 1.5;
            font-size: 0.95rem;
            white-space: pre-wrap;
        }
        .message.bot {
            align-self: flex-start;
            background: var(--bot-bubble);
            color: var(--text);
            border-bottom-left-radius: 4px;
        }
        .message.user {
            align-self: flex-end;
            background: var(--user-bubble);
            color: white;
            border-bottom-right-radius: 4px;
        }
        .chat-input-bar {
            padding: 1rem 1.25rem;
            background: var(--card);
            border-top: 1px solid var(--border);
            display: flex;
            gap: 0.75rem;
        }
        .chat-input-bar input {
            flex: 1;
            padding: 0.75rem 1rem;
            border: 1px solid var(--border);
            border-radius: 24px;
            outline: none;
            font-size: 0.95rem;
            font-family: inherit;
        }
        .chat-input-bar input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(4, 120, 87, 0.15);
        }
        .chat-input-bar button {
            background: var(--primary);
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 24px;
            font-weight: 600;
            cursor: pointer;
            font-family: inherit;
            transition: background 0.2s;
        }
        .chat-input-bar button:hover {
            background: var(--primary-dark);
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <div class="header-title">
                <h2>🏛️ உரிமை AI — உரையாடல் பதிவு</h2>
                <p>தமிழ்நாடு அரசு நலத்திட்ட வழிகாட்டி</p>
            </div>
            <div class="session-badge" id="session-badge">Session: Initializing...</div>
        </div>
        <div class="chat-messages" id="chat-messages">
            <div class="message bot">வணக்கம்! உரிமை AI உதவி மையத்திற்கு உங்களை வரவேற்கிறோம். தங்களின் குடும்ப விவரங்களை பதிவு செய்து தகுதியான நலத்திட்டங்களை கண்டறியலாம். தொடங்குவோமா?</div>
        </div>
        <div class="chat-input-bar">
            <input type="text" id="user-input" placeholder="தங்கள் பதிலை தமிழில் தட்டச்சு செய்யவும்... (எ.கா: ஆம்)" autofocus>
            <button id="send-btn" onclick="sendMessage()">அனுப்பு</button>
        </div>
    </div>

    <script>
        const sessionId = "session_" + Math.random().toString(36).substring(2, 10);
        document.getElementById("session-badge").innerText = sessionId;

        const messagesContainer = document.getElementById("chat-messages");
        const inputField = document.getElementById("user-input");

        inputField.addEventListener("keypress", function(e) {
            if (e.key === "Enter") {
                sendMessage();
            }
        });

        async function sendMessage() {
            const text = inputField.value.trim();
            if (!text) return;

            appendMessage(text, "user");
            inputField.value = "";
            inputField.focus();

            try {
                const response = await fetch("/intake/message", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ session_id: sessionId, message: text })
                });

                const data = await response.json();
                appendMessage(data.reply, "bot");
            } catch (err) {
                appendMessage("மன்னிக்கவும், தகவல் தொடர்பில் பிழை ஏற்பட்டது. தயவுசெய்து மீண்டும் முயற்சிக்கவும்.", "bot");
            }
        }

        function appendMessage(text, role) {
            const msgDiv = document.createElement("div");
            msgDiv.className = "message " + role;
            msgDiv.innerText = text;
            messagesContainer.appendChild(msgDiv);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
    </script>
</body>
</html>
"""
    return html_content
