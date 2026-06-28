"""
chatbot_gui.py
---------------
TKINTER GUI version of the Rule-Based Chatbot.

Run this file with:
    python chatbot_gui.py

It opens a chat window with:
    - A scrollable chat display area (shows the full conversation)
    - A text entry box for typing messages
    - A "Send" button (and pressing Enter also sends the message)
    - A "Clear Chat" button

Just like chatbot_console.py, this file only handles the INTERFACE.
All the actual "thinking" still happens in chatbot_logic.py.
"""

import tkinter as tk
from tkinter import scrolledtext
from chatbot_logic import get_response, BOT_NAME


# -------------------------------------------------------------
# COLORS & FONTS - kept as variables at the top so the look of
# the app can be changed easily in one place.
# -------------------------------------------------------------
BG_COLOR = "#1e1e2f"        # Main window background
CHAT_BG = "#2b2b3d"         # Chat display background
USER_COLOR = "#4fc3f7"      # Color for "You" label
BOT_COLOR = "#81c784"       # Color for bot's name label
ENTRY_BG = "#3a3a4d"        # Input box background
TEXT_COLOR = "#f5f5f5"      # General text color
FONT_MAIN = ("Segoe UI", 11)
FONT_TITLE = ("Segoe UI", 16, "bold")


class ChatbotGUI:
    """
    This class builds and manages the entire chatbot window.
    Using a class keeps all the widgets and functions related to
    the GUI neatly organized together.
    """

    def __init__(self, root):
        self.root = root
        self.root.title(f"{BOT_NAME} - Rule Based Chatbot")
        self.root.geometry("480x600")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self._build_widgets()   # Create all buttons, boxes, labels etc.

    # -----------------------------------------------------------
    # WIDGET CREATION
    # -----------------------------------------------------------
    def _build_widgets(self):
        """Create and arrange every widget in the window."""

        # ---- Title bar at the top ----
        title_label = tk.Label(
            self.root, text=f"🤖 {BOT_NAME}", font=FONT_TITLE,
            bg=BG_COLOR, fg="white", pady=10
        )
        title_label.pack(fill="x")

        # ---- Chat display area (scrollable + read-only) ----
        self.chat_area = scrolledtext.ScrolledText(
            self.root, wrap=tk.WORD, bg=CHAT_BG, fg=TEXT_COLOR,
            font=FONT_MAIN, state="disabled", padx=10, pady=10,
            borderwidth=0
        )
        self.chat_area.pack(padx=10, pady=(0, 10), fill="both", expand=True)

        # Tags let us color "You:" and "PyBot:" labels differently
        self.chat_area.tag_config("user", foreground=USER_COLOR,
                                   font=(FONT_MAIN[0], 11, "bold"))
        self.chat_area.tag_config("bot", foreground=BOT_COLOR,
                                   font=(FONT_MAIN[0], 11, "bold"))
        self.chat_area.tag_config("msg", foreground=TEXT_COLOR)

        # ---- Bottom frame: holds the entry box + Send button side by side ----
        bottom_frame = tk.Frame(self.root, bg=BG_COLOR)
        bottom_frame.pack(fill="x", padx=10, pady=(0, 10))

        self.entry_box = tk.Entry(
            bottom_frame, font=FONT_MAIN, bg=ENTRY_BG, fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR, relief="flat"
        )
        self.entry_box.pack(side="left", fill="x", expand=True, padx=(0, 5), ipady=6)
        # Pressing the Enter key also sends the message
        self.entry_box.bind("<Return>", lambda event: self.send_message())
        self.entry_box.focus()   # Cursor starts inside the input box

        send_btn = tk.Button(
            bottom_frame, text="Send", command=self.send_message,
            bg=USER_COLOR, fg="black", font=FONT_MAIN, relief="flat", padx=10
        )
        send_btn.pack(side="left")

        # ---- Clear Chat button (full width, below everything) ----
        clear_btn = tk.Button(
            self.root, text="Clear Chat", command=self.clear_chat,
            bg="#e57373", fg="black", font=FONT_MAIN, relief="flat", pady=4
        )
        clear_btn.pack(fill="x", padx=10, pady=(0, 10))

        # Show a welcome message as soon as the window opens
        self._display_message(BOT_NAME, "Hello! I'm your rule-based chatbot. Ask me anything 😊", "bot")

    # -----------------------------------------------------------
    # HELPER METHODS
    # -----------------------------------------------------------
    def _display_message(self, sender, message, tag):
        """
        Insert one message into the chat display area.
        'tag' decides the color/style used ("user" or "bot").
        """
        self.chat_area.configure(state="normal")        # Temporarily unlock for editing
        self.chat_area.insert(tk.END, f"{sender}: ", tag)
        self.chat_area.insert(tk.END, f"{message}\n\n", "msg")
        self.chat_area.configure(state="disabled")       # Lock it again (read-only)
        self.chat_area.see(tk.END)                        # Auto-scroll to the newest message

    def send_message(self):
        """
        Called when the user clicks 'Send' or presses Enter.
        Reads the typed text, shows it, asks chatbot_logic for a
        reply, then displays that reply too.
        """
        user_text = self.entry_box.get().strip()

        if user_text == "":
            return   # Do nothing if the input box is empty

        self._display_message("You", user_text, "user")
        self.entry_box.delete(0, tk.END)   # Clear the input box for the next message

        response, should_exit = get_response(user_text)   # Ask the chatbot's brain
        self._display_message(BOT_NAME, response, "bot")

        if should_exit:
            # If the user said goodbye, lock the input box so chat ends gracefully
            self.entry_box.configure(state="disabled")

    def clear_chat(self):
        """Erase every message currently shown in the chat area."""
        self.chat_area.configure(state="normal")
        self.chat_area.delete("1.0", tk.END)
        self.chat_area.configure(state="disabled")
        self._display_message(BOT_NAME, "Chat cleared! Let's start fresh 😊", "bot")


def main():
    """Entry point of the GUI program - creates the window and runs it."""
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
