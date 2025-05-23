import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid positive integer for length.")


root = tk.Tk()
root.title("Password Generator")
root.geometry("300x300")
root.config(bg="skyblue")


tk.Label(root, text="Enter password length:",bg="pink").pack(pady=10)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password,bg="pink",activebackground="purple")
generate_button.pack(pady=20)

result_label = tk.Label(root, text="Generated Password will appear here.",bg="violet")
result_label.pack(pady=20)

root.mainloop()
