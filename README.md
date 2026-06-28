<div align="center">

# 🤖 Rule-Based Chatbot with Predefined Responses

### A Beginner-to-Production-Style Conversational AI Built on Pure Python Logic

*Demonstrating the fundamentals of Natural Language Processing, Decision Logic, and Conversational System Design — no Machine Learning, no external APIs, no internet required.*

[![Python Version](https://img.shields.io/badge/Python-3.7%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#-license)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](#)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-orange?style=for-the-badge)](#)
[![ML Free](https://img.shields.io/badge/Machine%20Learning-Not%20Used-lightgrey?style=for-the-badge)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](#)

</div>

---

## 🧭 Project Overview

**Rule-Based Chatbot with Predefined Responses** is a lightweight, fully offline conversational agent built entirely with core Python. It simulates human-like dialogue by mapping user input to a curated set of **rules** — keyword patterns paired with appropriate responses — rather than relying on trained machine learning models or third-party AI APIs.

This project is intentionally engineered to be **transparent and explainable**: every decision the chatbot makes can be traced back to a specific, human-readable rule. It serves as both a practical conversational tool and an educational reference implementation of how early-generation chatbots (e.g. ELIZA-style systems) and many production rule engines and FAQ bots still operate today.

> 💡 **In one sentence:** A chatbot that listens for keywords in your message and replies using carefully designed rules — built with two interchangeable interfaces (Console + GUI) sharing one decision-making core.

---

## 📝 Project Description

Modern conversational AI is often associated with deep learning and large language models — but the discipline began with **deterministic, rule-based systems**, and that foundation remains critical for understanding how dialogue systems route, validate, and respond to user intent.

This project builds a chatbot that:

- Accepts free-text input from a user (via terminal or GUI)
- Normalizes and analyzes that input using **keyword and pattern matching**
- Selects an appropriate response using **conditional decision logic**
- Handles greetings, FAQs, date/time queries, gratitude, and farewells
- Gracefully manages **unrecognized input** with a fallback response
- Terminates the conversation politely on command

The codebase cleanly separates **logic** from **interface** — the chatbot's "brain" (`chatbot_logic.py`) is completely independent of how the user interacts with it, allowing the exact same decision engine to power both a terminal application and a desktop GUI application without duplicating a single rule.

---

## ✨ Features

| Capability | Description |
|---|---|
| 👋 **Greeting Detection** | Recognizes variations of "hello", "hi", "hey", "good morning", etc. |
| 🏷️ **Identity Response** | Answers questions like "what is your name?" |
| 🙂 **Wellbeing Check** | Responds naturally to "how are you?" |
| 🕒 **Live Date & Time** | Computes and returns the current date/time on request |
| 🎓 **Domain FAQ Handling** | Answers basic college/branch-related queries |
| 🧠 **AI/ML Awareness** | Explains basic AI and Machine Learning concepts on request |
| 🙏 **Gratitude Recognition** | Responds appropriately to "thank you" / "thanks" |
| 👋 **Graceful Exit** | Ends the conversation cleanly on "bye" / "exit" / "quit" |
| ❓ **Fallback Handling** | Returns a sensible default reply for unrecognized input — never crashes |
| 🖥️ **Dual Interface** | Fully functional Console (CLI) and Tkinter GUI versions |
| 🎨 **Polished GUI** | Dark-themed chat window with color-coded messages, Send & Clear Chat buttons |
| ⚙️ **Zero Dependencies** | Built entirely on the Python Standard Library — nothing to `pip install` |

---

## 🛠️ Technologies Used

| Category | Technology |
|---|---|
| Language | **Python 3.7+** |
| Logic & Pattern Matching | Native Python (`if/elif/else`, string methods, substring search) |
| Data Modeling | Python `dict` and `list` structures |
| Date/Time Handling | `datetime` (standard library) |
| Response Variation | `random` (standard library) |
| GUI Framework | `tkinter` + `tkinter.scrolledtext` (standard library) |
| Version Control | Git & GitHub |
| Documentation | Markdown |

> No third-party packages, no API keys, no internet connection required — the entire system runs offline using only what ships with Python.

---

## 📂 Project Structure

```
chatbot-project/
│
├── chatbot_logic.py           # 🧠 Core chatbot brain — rules, keyword matching, response logic
├── chatbot_console.py         # 💻 Terminal (CLI) interface
├── chatbot_gui.py             # 🪟 Tkinter desktop GUI interface
├── README.md                  # 📘 You are here
├── PROJECT_DOCUMENTATION.md   # 📑 In-depth report: algorithm, flowchart, viva Q&A, etc.
└── screenshots/               # 🖼️ Visual demos of the console & GUI in action
```

**Design principle:** `chatbot_logic.py` has zero knowledge of *how* it's being used — both `chatbot_console.py` and `chatbot_gui.py` simply import `get_response()` and render the output in their own way. This is a textbook example of **separation of concerns**.

---

## ⚙️ Installation Guide

### Prerequisites
- Python **3.7 or higher** installed on your system
- `pip` (optional — not actually required for this project, but good to have)

### Step 1 — Clone the Repository

```bash
git clone https://github.com/<your-username>/rule-based-chatbot-python.git
cd rule-based-chatbot-python
```

### Step 2 — (Linux only) Ensure Tkinter is Installed

Tkinter ships with Python on Windows and macOS. On some Linux distributions it must be installed separately:

```bash
sudo apt-get update
sudo apt-get install python3-tk
```

### Step 3 — Verify Your Python Installation

```bash
python --version
```

No `requirements.txt` is needed — this project has **zero external dependencies**.

---

## ▶️ How to Run the Project

### 🖥️ Console Version

```bash
python chatbot_console.py
```

You'll be greeted with a welcome banner. Type any message and press **Enter**. Type `bye`, `exit`, or `quit` to end the session.

### 🪟 GUI Version

```bash
python chatbot_gui.py
```

This launches a desktop chat window with:
- A scrollable conversation history
- A text input field
- A **Send** button (or press **Enter**)
- A **Clear Chat** button to reset the conversation

---

## ⚙️ Working Principle

```
User Input → Text Normalization → Keyword Matching → Rule Selection → Response Generation → Output
```

1. The user submits a message (console input or GUI entry box).
2. The message is **normalized**: converted to lowercase, trimmed of whitespace.
3. The system checks for **special cases** first (e.g. date/time queries, which require a calculated answer rather than a static one).
4. The normalized text is scanned against a **dictionary of rule categories**, each holding a list of trigger keywords.
5. On a match, a response is randomly selected from that category's predefined response pool (for natural variation).
6. If no rule matches, a **default fallback response** is returned — the chatbot never fails silently or crashes on unexpected input.
7. If the matched category is a farewell, the calling interface is signaled to **end the conversation** gracefully.

---

## 🏗️ Chatbot Architecture

```
                ┌────────────────────────┐
                │   User Interfaces      │
                │ ┌────────┐ ┌──────────┐│
                │ │Console │ │  Tkinter ││
                │ │  CLI   │ │   GUI    ││
                │ └───┬────┘ └────┬─────┘│
                └─────┼───────────┼──────┘
                       │           │
                       ▼           ▼
              ┌────────────────────────────┐
              │      chatbot_logic.py      │
              │   (Single Source of Truth) │
              │  ┌───────────────────────┐ │
              │  │  Input Normalization  │ │
              │  ├───────────────────────┤ │
              │  │  Keyword Matching     │ │
              │  │  Engine (RULES dict)  │ │
              │  ├───────────────────────┤ │
              │  │  Date/Time Generator  │ │
              │  ├───────────────────────┤ │
              │  │  Response Selector    │ │
              │  │  (random.choice)      │ │
              │  ├───────────────────────┤ │
              │  │  Fallback Handler     │ │
              │  └───────────────────────┘ │
              └────────────────────────────┘
```

The architecture follows a **single-core, multi-interface pattern**: one decision engine, multiple front-ends — a pattern commonly used in real-world conversational platforms where the same intent-handling logic powers web chat, mobile apps, and voice assistants.

---

## 🔬 NLP Concepts Used

While this project does not use a full NLP pipeline (tokenizers, embeddings, parsers, etc.), it demonstrates the **foundational building blocks** that modern NLP systems are built on:

| Concept | How It's Applied Here |
|---|---|
| **Text Normalization** | Lowercasing and trimming input before analysis — a standard NLP preprocessing step |
| **Keyword / Lexical Matching** | Detecting the presence of specific tokens or phrases within a string |
| **Intent Recognition (simplified)** | Mapping recognized keywords to a discrete conversational "intent" category (greeting, farewell, FAQ, etc.) |
| **Pattern Matching** | Using substring search as a lightweight stand-in for regex/NLP-based pattern recognition |
| **Response Generation** | Selecting from a curated response pool — analogous to template-based natural language generation (NLG) |
| **Fallback / Out-of-Scope Handling** | A core requirement in real NLP systems — gracefully handling unrecognized input rather than failing |

This makes the project an excellent **conceptual stepping stone** before moving to intent classifiers, NLTK/spaCy pipelines, or transformer-based chatbots.

---

## 🧩 Rule-Based Response System Explanation

At the heart of this chatbot is a single Python dictionary, `RULES`, structured like this:

```python
RULES = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning"],
        "responses": [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
        ]
    },
    # ... additional categories
}
```

**How matching works, step by step:**

1. The chatbot loops through every **category** in `RULES` (e.g. `greeting`, `name`, `college`, `ai`, `thanks`, `goodbye`).
2. For each category, it loops through that category's **keyword list**.
3. If any keyword is found as a **substring** of the user's (lowercased) message, that category is considered "matched."
4. Once matched, the chatbot uses `random.choice()` to select one reply from that category's response list — avoiding robotic repetition.
5. If the matched category is `goodbye`, the system also signals the interface to end the session.
6. If **no category matches at all**, a default fallback message is returned.

**Why this approach works well for a defined domain:**
- It's **fully deterministic and explainable** — you can predict exactly why a given response was triggered.
- It requires **no training data or GPU compute** — pure conditional logic.
- It's **trivially extensible** — adding a new topic means adding a new dictionary entry, with zero changes to the matching engine itself.

---

## 💬 Example Conversation

```
==================================================
  Welcome to PyBot - Rule Based Chatbot
==================================================
Type 'bye' / 'exit' / 'quit' anytime to stop chatting.

You: hello
PyBot: Hi there! What can I do for you?

You: what is your name
PyBot: I am PyBot, your friendly rule-based chatbot!

You: what time is it
PyBot: Right now it is: Monday, 22 June 2026 | 05:57 PM

You: what is machine learning
PyBot: Machine Learning is a part of AI where computers learn patterns
from data instead of being given a fixed rule for every situation.
This chatbot, though, uses simple rules - not machine learning!

You: thanks
PyBot: You're welcome!

You: bye
PyBot: Goodbye! Have a great day ahead.
```
---

## 🧱 Code Structure Explanation

### `chatbot_logic.py` — The Core Engine
- `RULES` — dictionary mapping each conversational category to its keywords and response pool
- `DEFAULT_RESPONSES` — fallback replies for unmatched input
- `is_date_time_query()` — detects date/time-related questions
- `get_date_time_response()` — generates a live, formatted timestamp
- `match_category()` — the keyword-matching engine; loops through `RULES` to find the right category
- `get_response()` — the single public function both interfaces call; returns `(reply_text, should_exit)`

### `chatbot_console.py` — Terminal Interface
- `print_welcome()` — displays a startup banner
- `chat()` — the main `while True` loop driving the conversation via `input()` / `print()`

### `chatbot_gui.py` — Tkinter GUI Interface
- `ChatbotGUI` class — encapsulates the entire window
- `_build_widgets()` — constructs the chat display, entry box, Send and Clear Chat buttons
- `send_message()` — handles user submissions and renders bot replies
- `clear_chat()` — resets the chat history
- `main()` — bootstraps the Tkinter event loop

---

## 🚀 Future Improvements

- 🧠 Integrate lightweight NLP (NLTK / spaCy) for stemming, tokenization, and intent classification
- 💾 Persist conversation history to a file or database
- 🗣️ Add speech-to-text and text-to-speech support for voice interaction
- 🌐 Connect to an LLM/NLP API for open-domain questions, layered on top of the existing rule engine as a hybrid system
- 🗂️ Externalize rules into a JSON/YAML config file so non-developers can edit chatbot knowledge
- 🧪 Add a unit test suite (`pytest`) covering all rule categories
- 🌍 Add multi-language support

---

## 🎓 Learning Outcomes

By completing this project, you will be able to:

- Apply core Python control structures (`if/elif/else`, `for`, `while`) to build a real, interactive application
- Design and use **dictionaries of dictionaries** to model structured knowledge
- Implement basic **keyword-based pattern matching** for text analysis
- Understand the architectural principle of **separating business logic from UI**
- Build a working **Tkinter desktop GUI** application from scratch
- Document a software project to a professional, industry-acceptable standard

---

## 🌍 Applications

This rule-based approach — while simple — directly mirrors techniques used in:

- 🏢 **Customer support FAQ bots** for websites and apps
- 🏦 **Banking/IVR systems** that route queries based on fixed menus and keywords
- 🎓 **Educational chatbots** for answering common student queries
- 🛍️ **E-commerce order-status bots** that handle a fixed set of predictable questions
- 🤖 **Fallback layers** inside larger AI systems, used when a model's confidence is low

---

## ✅ Advantages

- Fully **offline** — no internet, API key, or cloud dependency
- **Lightweight and fast** — instant responses, no model loading time
- **Predictable and explainable** — every response can be traced to a specific rule
- **Beginner-friendly** — readable, well-commented code ideal for learning
- **Easily extensible** — new topics require only a new dictionary entry

---

## ⚠️ Limitations

- Cannot understand sentence **meaning or grammar** — only keyword presence
- No **conversational memory** — each message is processed independently
- Sensitive to **typos and unanticipated phrasing**
- Not designed to scale to **hundreds of overlapping topics** without conflicts
- Cannot perform **reasoning, summarization, or generation** beyond pre-written text

---

## 🧠 Skills Demonstrated

`Python Programming` `Conditional Logic` `Dictionaries & Data Structures` `Functions & Modular Design` `Keyword/Pattern Matching` `Tkinter GUI Development` `Software Architecture (Separation of Concerns)` `Technical Documentation` `Git & GitHub` `Problem Solving`

---

<div align="center">
</div>
