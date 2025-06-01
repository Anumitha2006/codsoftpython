import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Core choices
choices = ["Rock", "Paper", "Scissors"]

# Function to determine winner
def determine_winner(user, comp):
    if user == comp:
        return "It's a tie!"
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Scissors" and comp == "Paper") or \
         (user == "Paper" and comp == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle play
def play(choice):
    user_choice.set(choice)
    comp = random.choice(choices)
    comp_choice.set(comp)
    result.set(determine_winner(choice, comp))

    # Update images
    user_image_label.config(image=image_map[choice])
    user_image_label.image = image_map[choice]

    comp_image_label.config(image=image_map[comp])
    comp_image_label.image = image_map[comp]

# Tkinter window setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="lightgreen")  

# Load and resize images
rock_img = ImageTk.PhotoImage(Image.open("C:/Users/LENOVO/Downloads/Untitled design.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("C:/Users/LENOVO/Downloads/Untitled design (1).png").resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open("C:/Users/LENOVO/Downloads/Untitled design (2).png").resize((100, 100)))

# Map choices to images
image_map = {
    "Rock": rock_img,
    "Paper": paper_img,
    "Scissors": scissors_img
}

# Game state variables
user_choice = tk.StringVar()
comp_choice = tk.StringVar()
result = tk.StringVar()

# Title
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"),bg='lightgreen').pack(pady=10)

# Button section
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, image=rock_img, command=lambda: play("Rock")).grid(row=0, column=0, padx=10)
tk.Button(button_frame, image=paper_img, command=lambda: play("Paper")).grid(row=0, column=1, padx=10)
tk.Button(button_frame, image=scissors_img, command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

# User choice display
tk.Label(root, text="Your Choice:", font=("Arial", 14),bg='lightgreen').pack(pady=(20, 5))
user_image_label = tk.Label(root)
user_image_label.pack()

# Computer choice display
tk.Label(root, text="Computer's Choice:", font=("Arial", 14),bg='lightgreen').pack(pady=(20, 5))
comp_image_label = tk.Label(root)
comp_image_label.pack()

# Choices text
tk.Label(root, textvariable=comp_choice, font=("Arial", 12),bg='lightgreen').pack()
tk.Label(root, text="Result:", font=("Arial", 14),bg='lightgreen').pack(pady=5)
tk.Label(root, textvariable=result, font=("Arial", 14), fg="blue",bg='lightgreen').pack()

# Exit button
tk.Button(root, text="Exit", font=("Arial", 12), command=root.quit,bg='lightgreen').pack(pady=10)

# Start GUI
root.mainloop()
