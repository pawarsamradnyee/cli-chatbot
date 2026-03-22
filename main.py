from llm import get_response
from memory import (
    get_initial_messages,
    add_user_message,
    add_ai_message,
    trim_messages
)

def choose_mode():
    print("Choose chatbot mode:")
    print("1. Short")
    print("2. Detailed")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        return "short"
    return "detailed"

def run_chat():
    print("🤖 CLI Chatbot")
    print("Type 'exit' to quit\n")

    mode = choose_mode()
    messages = get_initial_messages(mode)

    print(f"\nChatbot started in '{mode}' mode.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break

        if not user_input:
            print("Please type something.\n")
            continue

        add_user_message(messages, user_input)

        # keep memory under control before API call
        messages = trim_messages(messages)

        print("\nThinking...\n")

        response = get_response(messages)

        add_ai_message(messages, response)

        print("AI:", response)
        print()

if __name__ == "__main__":
    run_chat()