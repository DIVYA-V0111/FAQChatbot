
import tkinter as tk
from tkinter import scrolledtext
from chatbot import get_answer


def send_message(event=None):
    question = input_entry.get().strip()

    if not question:
        return "break"

    chat_area.config(state="normal")
    chat_area.insert(tk.END, "You: " + question + "\n")
    
    answer = get_answer(question)
    chat_area.insert(tk.END, "Chatbot: " + answer + "\n\n")
    
    chat_area.config(state="disabled")
    chat_area.see(tk.END)

    input_entry.delete(0, tk.END)
    input_entry.focus()

    return "break"


def clear_chat():
    chat_area.config(state="normal")
    chat_area.delete("1.0", tk.END)
    chat_area.insert(tk.END, "Chatbot: Hello! Ask me a college-related question.\n\n")
    chat_area.config(state="disabled")


# Create the main window
root = tk.Tk()
root.title("College FAQ Chatbot")
root.geometry("650x550")
root.configure(bg="#f0f4f8")

# Heading
heading = tk.Label(
    root,
    text="College FAQ Chatbot",
    font=("Arial", 20, "bold"),
    bg="#f0f4f8",
    fg="#1f3c5b"
)
heading.pack(pady=15)

# Chat display area
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 11),
    bg="white",
    fg="#222222",
    state="disabled"
)
chat_area.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)

# Input area
input_frame = tk.Frame(root, bg="#f0f4f8")
input_frame.pack(fill=tk.X, padx=15, pady=10)

input_entry = tk.Entry(
    input_frame,
    font=("Arial", 12)
)
input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)
input_entry.bind("<Return>", send_message)

send_button = tk.Button(
    input_frame,
    text="Send",
    font=("Arial", 11, "bold"),
    bg="#2563eb",
    fg="white",
    command=send_message
)
send_button.pack(side=tk.LEFT, padx=(8, 0))

# Clear button
clear_button = tk.Button(
    root,
    text="Clear Chat",
    font=("Arial", 10),
    command=clear_chat
)
clear_button.pack(pady=(0, 12))

# Welcome message
clear_chat()
input_entry.focus()

root.mainloop()
