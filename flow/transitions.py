from flow.states import State
from tools.phone_validator import validate_phone_number

def get_next_state(current_state, user_input):
    if current_state == State.COLLECT_CITY:
        if "bangalore" in user_input.lower():
            return State.COLLECT_CONTACT
        return State.COLLECT_CITY

    elif current_state == State.COLLECT_CONTACT:
        if validate_phone_number(user_input):
            return State.END
        return State.COLLECT_CONTACT

    return current_state
