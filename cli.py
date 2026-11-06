from config import APP_NAME

def show_banner():
    print("=" * 58)
    print(APP_NAME.center(58))
    print("Ask questions about Python, AI, technology and computers.")
    print("Commands: clear memory | bye")
    print("=" * 58)

def run_terminal(assistant):
    show_banner()
    while True:
        try:
            message = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAssistant: Goodbye!")
            break

        if not message:
            continue

        answer = assistant.reply(message)
        print(f"\nAssistant: {answer}")

        if message.lower().strip() in {"bye", "goodbye", "exit", "quit", "close"}:
            break
