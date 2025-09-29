import tkinter as tk
from tkinter import messagebox
import random

# Dice images
DICE_IMAGES = [
    "🎲1", "🎲2", "🎲3", "🎲4", "🎲5", "🎲6"
]

class DiceGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Game")
        self.root.geometry("300x300")

        self.label1 = tk.Label(root, text="🎲 Dice Rolling Game 🎲", font=("Arial", 14))
        self.label1.pack(pady=10)

        self.dice_label1 = tk.Label(root, text="❓", font=("Arial", 50))
        self.dice_label1.pack()

        self.dice_label2 = tk.Label(root, text="❓", font=("Arial", 50))
        self.dice_label2.pack()

        self.roll_button = tk.Button(root, text="Roll Dice!", command=self.roll_dice, font=("Arial", 12))
        self.roll_button.pack(pady=20)

    def roll_dice(self):
        player1_roll = random.randint(1, 6)
        player2_roll = random.randint(1, 6)

        self.dice_label1.config(text=DICE_IMAGES[player1_roll - 1])
        self.dice_label2.config(text=DICE_IMAGES[player2_roll - 1])

        if player1_roll > player2_roll:
            winner = "🎉 Player 1 wins!"
        elif player2_roll > player1_roll:
            winner = "🎉 Player 2 wins!"
        else:
            winner = "😲 It's a tie!"

        messagebox.showinfo("Result", winner)

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = DiceGame(root)
    root.mainloop()
