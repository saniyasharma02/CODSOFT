"""
chatbot_logic.py
-----------------
This file contains the CORE BRAIN of the rule-based chatbot.

It does NOT take input from keyboard or show anything on screen by itself.
It only contains the RULES and decides WHAT response to give for a given
message. This is called "separation of logic from interface" - a good
programming practice.

Both chatbot_console.py (terminal version) and chatbot_gui.py (Tkinter
window version) import this file and reuse the SAME rules, so we never
have to write the chatbot's "brain" twice.

No Machine Learning or external AI API is used here - everything is
plain Python: if-else style checks, loops, and dictionaries.
"""

import random
from datetime import datetime

# Name of our chatbot - used inside some responses
BOT_NAME = "ChatBot"

# -----------------------------------------------------------------
# RULES: a dictionary of categories.
# Each category stores:
#   "keywords"  -> list of trigger words/phrases (pattern matching)
#   "responses" -> list of possible replies (one is picked randomly)
# Using a dictionary like this makes it very easy to add a new
# category later without changing the rest of the program.
# -----------------------------------------------------------------
RULES = {

    "greeting": {
        "keywords": [
            "hello", "hi", "hey", "hii", "hiya",
            "good morning", "good afternoon", "good evening", "namaste"
        ],
        "responses": [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Nice to see you. Ask me anything.",
        ]
    },

    "name": {
        "keywords": [
            "your name", "who are you", "what should i call you", "what is your name"
        ],
        "responses": [
            f"I am {BOT_NAME}, your friendly rule-based chatbot!",
            f"You can call me {BOT_NAME}. I'm here to chat with you.",
        ]
    },

    "wellbeing": {
        "keywords": [
            "how are you", "how're you", "how are u", "how do you do", "whats up", "what's up"
        ],
        "responses": [
            "I'm just a program, but I'm running perfectly fine! How about you?",
            "I'm doing great, thanks for asking! How can I help?",
        ]
    },

    "college": {
        "keywords": [
            "college", "course", "branch", "btech", "b.tech",
            "cse", "department", "semester", "subject", "exam"
        ],
        "responses": [
            "You're a B.Tech CSE (AI) student, right? That branch mixes "
            "programming, math, and data - a great combo for building cool projects!",
            "B.Tech CSE with an AI specialization usually covers programming, "
            "data structures, machine learning basics, and problem-solving skills.",
        ]
    },

    "ai": {
        "keywords": [
            "what is ai", "artificial intelligence", "machine learning",
            "what is ml", "deep learning", "neural network"
        ],
        "responses": [
            "Artificial Intelligence (AI) is the field of making computers "
            "perform tasks that normally need human intelligence - like "
            "understanding language, recognizing images, or making decisions.",
            "Machine Learning is a part of AI where computers learn patterns "
            "from data instead of being given a fixed rule for every situation. "
            "This chatbot, though, uses simple rules - not machine learning!",
        ]
    },

    "thanks": {
        "keywords": ["thank you", "thanks", "thank u", "thx"],
        "responses": [
            "You're welcome!",
            "No problem, happy to help!",
            "Anytime! That's what I'm here for.",
        ]
    },

    "goodbye": {
        "keywords": ["bye", "goodbye", "see you", "exit", "quit", "good night"],
        "responses": [
            "Goodbye! Have a great day ahead.",
            "See you soon! Take care.",
            "Bye! It was nice chatting with you.",
        ]
    },
}

# Generic responses used only when NOTHING from RULES matches
DEFAULT_RESPONSES = [
    "I'm sorry, I didn't understand that. Could you rephrase?",
    "Hmm, I'm not trained to answer that yet. Try asking something else!",
    "I don't have an answer for that. Try asking about AI, college, or just say hi!",
]

# Words that signal a date/time question - handled separately because
# the reply must be CALCULATED (current time), not picked from a fixed list.
DATE_TIME_KEYWORDS = ["date", "time", "day today", "what time", "today's date"]


def is_date_time_query(text):
    """
    Check whether the user's message is asking about the current
    date or time.
    'text' is expected to already be lowercase.
    """
    for word in DATE_TIME_KEYWORDS:
        if word in text:
            return True
    return False


def get_date_time_response():
    """Build and return a friendly string with today's date and time."""
    now = datetime.now()                                  # Get current date & time
    formatted = now.strftime("%A, %d %B %Y | %I:%M %p")    # Format it nicely
    return f"Right now it is: {formatted}"


def match_category(text):
    """
    Go through every category in RULES one by one (loop), and check
    if any of its keywords appear inside the user's message
    (this is our "pattern matching" technique - simple substring search).

    Returns the matching category name (a string), or None if nothing matched.
    """
    for category, data in RULES.items():       # Loop 1: through each category
        for keyword in data["keywords"]:        # Loop 2: through each keyword
            if keyword in text:                 # Pattern match check
                return category
    return None


def get_response(user_input):
    """
    MAIN FUNCTION of the chatbot's brain.

    Input : user_input (raw string typed by the user)
    Output: a tuple -> (response_text, should_exit)

        response_text -> what the bot should say
        should_exit    -> True only when the conversation should end
                          (e.g. user said "bye")

    Both the console and GUI programs call this ONE function to get
    every reply - they never need to know HOW the reply was decided.
    """
    # Step 1: Clean up the input - lowercase + remove extra spaces.
    # This makes matching case-insensitive ("Hello" == "hello" == "HELLO").
    text = user_input.lower().strip()

    # Step 2: Handle empty input
    if text == "":
        return "Please type something so I can help you!", False

    # Step 3: Date/Time questions need a calculated answer, check first
    if is_date_time_query(text):
        return get_date_time_response(), False

    # Step 4: Try to match the message against our keyword rules
    category = match_category(text)

    # Step 5: If it's a goodbye, tell the caller to stop the chat loop
    if category == "goodbye":
        return random.choice(RULES["goodbye"]["responses"]), True

    # Step 6: Any other matched category -> pick a random reply for it
    if category is not None:
        return random.choice(RULES[category]["responses"]), False

    # Step 7: Nothing matched at all -> fall back to a default response
    return random.choice(DEFAULT_RESPONSES), False
    # Run chatbot_logic.py directly (optional)
if __name__ == "__main__":
    while True:
        text = input("You: ")

        response, should_exit = get_response(text)

        print("ChatBot:", response)

        if should_exit:
            break
