import tkinter as tk
import random

# ---------------- GAME LOGIC ----------------

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0


def play_game(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    # Show choices
    user_label.config(text=f"You chose: {user_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")

    # Decide winner
    if user_choice == computer_choice:
        result = "🤝 It's a Draw!"

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or
        (user_choice == "Paper" and computer_choice == "Rock")
        or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You Win!"
        user_score += 1

    else:
        result = "🤖 Computer Wins!"
        computer_score += 1

    result_label.config(text=result)

    score_label.config(
        text=f"Your Score: {user_score}    |    Computer Score: {computer_score}"
    )


def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    user_label.config(text="You chose: -")
    computer_label.config(text="Computer chose: -")
    result_label.config(text="Choose your move!")
    score_label.config(text="Your Score: 0    |    Computer Score: 0")


# ---------------- GUI ----------------

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("600x550")
window.resizable(False, False)

# Title
title_label = tk.Label(
    window,
    text="✊ ROCK PAPER SCISSORS ✋",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=25)

# Subtitle
subtitle = tk.Label(
    window,
    text="Choose your move!",
    font=("Arial", 15)
)
subtitle.pack(pady=5)

# Buttons frame
button_frame = tk.Frame(window)
button_frame.pack(pady=30)

rock_button = tk.Button(
    button_frame,
    text="✊ Rock",
    font=("Arial", 14, "bold"),
    width=12,
    height=2,
    command=lambda: play_game("Rock")
)
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(
    button_frame,
    text="📄 Paper",
    font=("Arial", 14, "bold"),
    width=12,
    height=2,
    command=lambda: play_game("Paper")
)
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(
    button_frame,
    text="✌️ Scissors",
    font=("Arial", 14, "bold"),
    width=12,
    height=2,
    command=lambda: play_game("Scissors")
)
scissors_button.grid(row=0, column=2, padx=10)

# User choice
user_label = tk.Label(
    window,
    text="You chose: -",
    font=("Arial", 14)
)
user_label.pack(pady=8)

# Computer choice
computer_label = tk.Label(
    window,
    text="Computer chose: -",
    font=("Arial", 14)
)
computer_label.pack(pady=8)

# Result
result_label = tk.Label(
    window,
    text="Choose your move!",
    font=("Arial", 20, "bold")
)
result_label.pack(pady=20)

# Score
score_label = tk.Label(
    window,
    text="Your Score: 0    |    Computer Score: 0",
    font=("Arial", 14, "bold")
)
score_label.pack(pady=10)

# Reset button
reset_button = tk.Button(
    window,
    text="🔄 Play Again",
    font=("Arial", 13, "bold"),
    width=15,
    command=reset_game
)
reset_button.pack(pady=20)

# Start application
window.mainloop()