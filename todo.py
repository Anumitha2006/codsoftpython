import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

tasks = []

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        update_display()
    else:
        messagebox.showwarning("Input Invalid", "Task cannot be empty! Enter some task.")
    task_entry.delete(0, tk.END)

def delete_task():
    try:
        index = int(delete_entry.get()) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            update_display()
        else:
            messagebox.showerror("Error", "Task number invalid.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid task number.")
    delete_entry.delete(0, tk.END)  

def mark_completed():
    try:
        index = int(complete_entry.get()) - 1
        if 0 <= index < len(tasks):
            if not tasks[index].endswith("✓") and "[Completed]" not in tasks[index]:
                tasks[index] += " [Completed]"
                update_display()
            else:
                messagebox.showinfo("Info", "Task is already marked as completed.")
        else:
            messagebox.showerror("Error", "Task number invalid.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid task number.")
    complete_entry.delete(0, tk.END)

def update_display():
    task_list.config(state='normal')
    task_list.delete(1.0, tk.END)
    for i, task in enumerate(tasks, start=1):
        task_list.insert(tk.END, f"{i}. {task}\n")
    task_list.config(state='disabled')

# GUI Setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("600x400")

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(fill="both", expand=True)

# Load background image
bg_image = Image.open(r"C:\Users\LENOVO\Desktop\bg\Untitled design (2).png")
bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Title
title_label = tk.Label(root, text="TO-DO LIST", font=("Arial", 16, "bold"), bg="lightblue")
canvas.create_window(300, 30, window=title_label)

# Task entry
task_entry = tk.Entry(root, width=40)
canvas.create_window(220, 100, window=task_entry)

# Add button
add_button = tk.Button(root, text="Add Task",bg="lightblue", command=add_task)
canvas.create_window(400, 100, window=add_button)

# Delete task entry
delete_entry = tk.Entry(root, width=20)
delete_entry.insert(0, " ")
canvas.create_window(200, 140, window=delete_entry)

# Delete button
delete_button = tk.Button(root, text="Delete Task",bg="lightblue", command=delete_task)
canvas.create_window(400, 140, window=delete_button)

# Complete task entry
complete_entry = tk.Entry(root, width=20)
complete_entry.insert(0, " ")
canvas.create_window(200, 170, window=complete_entry)

# Complete button
complete_button = tk.Button(root, text="Mark Completed",bg="lightblue", command=mark_completed)
canvas.create_window(400, 170, window=complete_button)

# Display task list
task_list = tk.Text(root, width=50, height=10, state='disabled')
canvas.create_window(330, 270, window=task_list)

root.mainloop()
