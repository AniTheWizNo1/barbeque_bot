from fastapi import FastAPI, Body
from pydantic import BaseModel
from knowledge_base import query_kb
from flow.state_manager import detect_intent
from flow.state_manager import get_user_state, set_user_state
from prompts.loader import render_prompt

from logger import log_to_sheet
app = FastAPI()

class UserQuery(BaseModel):
    user_input: str

@app.post("/chat")
async def chat(query: UserQuery = Body(...)):
    user_id = "demo-user"  # Can be replaced with real phone/email
    state = get_user_state(user_id)

    intent, location, prompt = detect_intent(query.user_input)

    if intent:
        kb_response = query_kb(intent, location)
        final = render_prompt(f"{prompt}.jinja", {
            "location": location.title(),
            "response": kb_response
        })
        # Transition logic example
        if intent == "menu":
            set_user_state(user_id, "asked_menu")
        elif intent == "booking_request":
            set_user_state(user_id, "collecting_booking")
        log_to_sheet("chatbot",query.user_input,final)
    else:
        final = "Can you please clarify your request?"

    return {"response": final}
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
