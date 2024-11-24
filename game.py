import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0
        self.label_user_choice = tk.Label(root, text="Your choice:", font=("Arial", 14))
        self.label_user_choice.pack(pady=10)
        self.label_computer_choice = tk.Label(root, text="Computer's choice:", font=("Arial", 14))
        self.label_computer_choice.pack(pady=10)

        self.button_rock = tk.Button(root, text="Rock", command=lambda: self.play_game("rock"))
        self.button_rock.pack(side=tk.LEFT, padx=20)

        self.button_paper = tk.Button(root, text="Paper", command=lambda: self.play_game("paper"))
        self.button_paper.pack(side=tk.LEFT, padx=20)

        self.button_scissors = tk.Button(root, text="Scissors", command=lambda: self.play_game("scissors"))
        self.button_scissors.pack(side=tk.LEFT, padx=20)

        self.label_result = tk.Label(root, text="", font=("Arial", 16))
        self.label_result.pack(pady=20)

        self.label_scores = tk.Label(root, text="Score: You - 0, Computer - 0", font=("Arial", 12))
        self.label_scores.pack(side=tk.RIGHT, padx=20)

    def play_game(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = self.determine_winner(user_choice, computer_choice)

        self.label_user_choice.config(text=f"Your choice: {user_choice}")
        self.label_computer_choice.config(text=f"Computer's choice: {computer_choice}")

        self.label_result.config(text=f"Result: {result}")

        if "win" in result:
            self.user_score += 1
        elif "lose" in result:
            self.computer_score += 1

        self.label_scores.config(text=f"Score: You - {self.user_score}, Computer - {self.computer_score}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "You win!"
        else:
            return "You lose!"

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
