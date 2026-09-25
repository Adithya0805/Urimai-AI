"""CLI Interactive Intake Tool for Urimai AI."""
import sys
import uuid
from app.database import SessionLocal, engine, Base
from app.seed_data import seed_database
from app.services.intake_state import create_initial_state
from app.services.intake_graph import process_user_turn


def run_cli():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    seed_database(db)

    session_id = f"cli_{uuid.uuid4().hex[:8]}"
    state = create_initial_state(session_id)

    print("=" * 60)
    print("🏛️  உரிமை AI — தமிழ்நாடு அரசு நலத்திட்ட உரையாடல் பதிவு")
    print("   Urimai AI Tamil Conversational Intake Agent (CLI)")
    print(f"   Session ID: {session_id}")
    print("=" * 60)

    # Initial start
    state = process_user_turn(state, "தொடங்கு", db)
    print(f"\n[உரிமை AI]:\n{state['reply']}\n")

    while not state.get("is_completed"):
        try:
            user_input = input("[நீங்கள்]: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit", "வெளியேறு"]:
                print("\nபதிவு நிறுத்தப்பட்டது. நன்றி!")
                break

            state = process_user_turn(state, user_input, db)
            print(f"\n[உரிமை AI]:\n{state['reply']}\n")

        except (KeyboardInterrupt, EOFError):
            print("\nமுடிந்தது.")
            break

    db.close()


if __name__ == "__main__":
    run_cli()
