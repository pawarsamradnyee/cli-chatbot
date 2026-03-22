MAX_MESSAGES = 10

def build_system_prompt(mode="detailed"):
    if mode == "short":
        return (
            "You are a smart AI assistant. "
            "Give short, clear answers in 2-4 lines. "
            "If useful, use bullet points."
        )
    return (
        "You are an intelligent, helpful AI assistant.\n"
        "Rules:\n"
        "- Give clear and structured answers\n"
        "- Use bullet points when useful\n"
        "- Give step-by-step explanation if the user asks for steps\n"
        "- For technical questions, include simple examples\n"
        "- Keep answers concise but helpful"
    )

def get_initial_messages(mode="detailed"):
    return [
        {
            "role": "system",
            "content": build_system_prompt(mode)
        }
    ]

def add_user_message(messages, user_input):
    messages.append({"role": "user", "content": user_input})

def add_ai_message(messages, ai_response):
    messages.append({"role": "assistant", "content": ai_response})

def trim_messages(messages):
    system_message = messages[0]
    recent_messages = messages[1:][-MAX_MESSAGES:]
    return [system_message] + recent_messages