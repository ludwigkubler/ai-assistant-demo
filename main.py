from assistant import build_response


def main() -> None:
    print("AI Assistant Demo")
    print("-----------------")
    print("Type a message and press ENTER. Type 'exit' to quit.\n")

    while True:
        user_message = input("You: ").strip()
        if user_message.lower() in {"exit", "quit"}:
            print("Assistant: Goodbye!")
            break

        result = build_response(user_message)
        if result["status"] != "ok":
            print("Assistant:", result["message"])
        else:
            print("Assistant:", result["message"])
        print()


if __name__ == "__main__":
    main()
