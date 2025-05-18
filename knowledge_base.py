import json

with open("structured_kb.json", "r", encoding="utf-8") as f:
    knowledge_base = json.load(f)

def query_kb(intent, location=None):
    intent = intent.lower()
    
    if intent == "menu":
        return "\n\n".join(knowledge_base.get("menu", {}).values())
    if intent in ["veg_starters", "non_veg_starters", "menu"]:
        return "\n\n".join(knowledge_base.get("menu", {}).values())

    if location:
        location = location.lower()
        for city in ["bangalore", "delhi"]:
            for branch, info in knowledge_base.get(city, {}).items():
                if location in branch.lower():
                    return info

    return "Sorry, I couldn’t find relevant information."
