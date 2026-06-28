"""
chatbot_console.py
--------------------
CONSOLE (terminal) version of the Rule-Based Chatbot.

Run this file with:
    python chatbot_console.py

Type 'bye', 'exit', or 'quit' anytime to end the conversation.

This file is only responsible for INPUT/OUTPUT (talking to the user
through the terminal). All the "thinking" happens inside
chatbot_logic.py, which this file imports.
"""

from chatbot_logic import get_response, BOT_NAME


def print_welcome():
    """Print a simple welcome banner when the program starts."""
    print("=" * 50)
    print(f"  Welcome to {BOT_NAME} - Rule Based Chatbot")
    print("=" * 50)
    print("Type 'bye' / 'exit' / 'quit' anytime to stop chatting.\n")


def chat():
    """
    Main chat loop.

    Keeps asking the user for a message (input) and printing the
    bot's reply (output), again and again, until the user decides
    to end the conversation.
    """
    print_welcome()

    while True:                                  # Loop runs until we 'break'
        user_input = input("You: ")               # 1. Get input from the user

        response, should_exit = get_response(user_input)  # 2. Ask the brain for a reply

        print(f"{BOT_NAME}: {response}")          # 3. Show the reply on screen

        if should_exit:                            # 4. Stop the loop if it was a goodbye
            break


# The check below means: "Only run chat() if this file is executed
# directly (python chatbot_console.py)". If someone imports this file
# from another script, chat() will NOT run automatically.
if __name__ == "__main__":
    chat()
