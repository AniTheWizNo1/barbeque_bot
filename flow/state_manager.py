from flow.states import State
from flow.transitions import get_next_state
from prompts.loader import render_prompt
from sessions.memory import session_store
from tools.phone_validator import validate_phone_number, format_phone_number
from kb.query import search_kb
def process_input(session_id, user_input):
    session = session_store.get(session_id, {"state": State.COLLECT_CITY})
    current_state = session["state"]
    name = session.get("name")
    phone = session.get("phone")

    # 1. City Collection
    if current_state == State.COLLECT_CITY:
        if "bangalore" in user_input.lower():
            session["state"] = State.COLLECT_CONTACT
            session_store[session_id] = session
            return render_prompt(State.COLLECT_CONTACT)
        else:
            return render_prompt(State.COLLECT_CITY)

    # 2. Contact Collection
    elif current_state == State.COLLECT_CONTACT:
        if not name:
            session["name"] = user_input.strip()
        elif not phone:
            if validate_phone_number(user_input):
                session["phone"] = user_input.strip()
            else:
                return "Invalid phone number. Please provide a 10-digit number."
        else:
            confirmed = user_input.strip().lower() in ["yes", "y"]
            if confirmed:
                session["state"] = State.END
                session_store[session_id] = session
                return "Thanks! Your info is saved."
            else:
                session["name"] = None
                session["phone"] = None
                return "Let's try again. What's your name?"

        session["state"] = State.COLLECT_CONTACT
        session_store[session_id] = session
        return render_prompt(
            State.COLLECT_CONTACT,
            user_input,
            name_collected=bool(session.get("name")),
            phone_collected=bool(session.get("phone")),
            confirmed=bool(session.get("name") and session.get("phone")),
            name=session.get("name", ""),
            formatted_phone=format_phone_number(session.get("phone", ""))
        )

    # 3. Knowledge Base (MASTER_INFORM)
    elif current_state == State.MASTER_INFORM:
        results = search_kb(user_input)
        session["state"] = State.END
        session_store[session_id] = session
        return render_prompt(
            State.MASTER_INFORM,
            user_input,
            kb_results=results
        )

    # 4. Fallback / Default
    next_state = get_next_state(current_state, user_input)
    session["state"] = next_state
    session_store[session_id] = session
    return render_prompt(next_state, user_input)
    from prompts.loader import render_prompt  # You’ll need to create this

def detect_intent(user_input: str):
    user_input = user_input.lower()

    if "veg" in user_input and "starter" in user_input:
        return "veg_starters", "bangalore", "answer_menu"
    if "menu" in user_input:
        return "menu", "bangalore", "answer_menu"

    return None, None, "fallback"
user_state = {}

def get_user_state(user_id):
    return user_state.get(user_id, "default")

def set_user_state(user_id, state):
    user_state[user_id] = state


