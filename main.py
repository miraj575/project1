
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time

# Function to display a message box
def show_message(title, message):
    messagebox.showinfo(title, message)

# Function to display the teddy bear GIF
def show_teddy_bear():
    gif_window = tk.Toplevel(root)
    gif_window.title("Teddy Bear Surprise!")

    gif_path = "path_to_your_gif.gif"  # Path to your local GIF file
    img = Image.open(gif_path)
    img = img.resize((250, 250))
    gif = ImageTk.PhotoImage(img)

    gif_label = tk.Label(gif_window, image=gif)
    gif_label.image = gif  # Keep a reference to avoid garbage collection
    gif_label.pack()

# Function to handle question responses
def handle_response(question_num, choice):
    responses = {
        (1, 'A'): "Snowy mountains! Just imagine us snuggling by the fireplace, sipping hot chocolate. ❄️",
        (1, 'B'): "Ah, the beach! Sun, sand, and waves—nothing better than chilling by the ocean with you. 🌴🌊",
        (1, 'C'): "A magical city! Walking hand in hand through cobblestone streets, discovering hidden gems. 🏙️",
        (2, 'A'): "A knight! You’d have shining armor and a heart of gold. 🛡️⚔️",
        (2, 'B'): "A wizard! Full of wisdom, you’d cast spells to protect us and solve ancient mysteries. 🔮",
        (2, 'C'): "A rogue! Quick and clever, always finding ways to outsmart any challenge. 🗡️💨",
        ('yes_1', 'yes'): "Aww! You trust me, huh? Well, get ready because a surprise is coming your way soon! 🎉",
        ('yes_1', 'no'): "Oh no! Looks like I need to work on my surprise skills. Don't worry, I'll prove you wrong! 😜",
        ('yes_2', 'yes'): "Amazing! Let’s teleport to a beautiful beach where we can relax together. 🌊☀️",
        ('yes_2', 'no'): "Not right now? That’s okay, we can teleport later to somewhere even more special. 🌍💫",
    }
    response = responses.get((question_num, choice))
    if not response:
        response = responses.get((question_num, 'default'), "Oops! That's not a valid choice.")
    show_message("Response", response)

# Function to handle the game flow
def start_game():
    question1_frame.pack_forget()
    yes_no_frame.pack()

def show_question_1():
    yes_no_frame.pack_forget()
    question1_frame.pack()

def show_question_2():
    question1_frame.pack_forget()
    show_teddy_bear()
    question2_frame.pack()

def show_conclusion():
    question2_frame.pack_forget()
    show_message("Thank You!", "✨ Thank you for playing 'Fairuz's Adventure!' ✨\nNo matter which paths you chose, one thing is clear:\nYou make every moment we share feel like an adventure. 💕\nHere's a final surprise for you... 🥁\n🌹 You are the most amazing person I’ve ever known, and every day with you is a gift. I’m so lucky to have you in my life, Fairuz. 💖\nLet’s create even more memories, one adventure at a time. 💑")

# Create the main window
root = tk.Tk()
root.title("Fairuz's Adventure")

# Frames for different sections
question1_frame = tk.Frame(root)
yes_no_frame = tk.Frame(root)
question2_frame = tk.Frame(root)

# Question 1
tk.Label(question1_frame, text="Question 1: Imagine we’re planning a dream vacation together. Where would you love to go?").pack()
tk.Button(question1_frame, text="A. A cozy cabin in the snowy mountains", command=lambda: handle_response(1, 'A')).pack()
tk.Button(question1_frame, text="B. A sunny beach resort on a tropical island", command=lambda: handle_response(1, 'B')).pack()
tk.Button(question1_frame, text="C. A magical city full of history and culture", command=lambda: handle_response(1, 'C')).pack()
tk.Button(question1_frame, text="Next", command=show_question_2).pack()

# Yes/No Questions
tk.Label(yes_no_frame, text="Yes/No Question: Would you trust me to plan a surprise date for us?").pack()
tk.Button(yes_no_frame, text="Yes", command=lambda: handle_response('yes_1', 'yes')).pack()
tk.Button(yes_no_frame, text="No", command=lambda: handle_response('yes_1', 'no')).pack()
tk.Button(yes_no_frame, text="Next", command=show_question_1).pack()

tk.Label(yes_no_frame, text="Yes/No Question: Would you like to teleport anywhere in the world with me right now?").pack()
tk.Button(yes_no_frame, text="Yes", command=lambda: handle_response('yes_2', 'yes')).pack()
tk.Button(yes_no_frame, text="No", command=lambda: handle_response('yes_2', 'no')).pack()

# Question 2
tk.Label(question2_frame, text="Question 2: If we were characters in a fantasy world, who would you be?").pack()
tk.Button(question2_frame, text="A. A brave knight, always ready for adventure", command=lambda: handle_response(2, 'A')).pack()
tk.Button(question2_frame, text="B. A wise wizard, mastering spells and secrets", command=lambda: handle_response(2, 'B')).pack()
tk.Button(question2_frame, text="C. A mischievous rogue, clever and always one step ahead", command=lambda: handle_response(2, 'C')).pack()
tk.Button(question2_frame, text="Finish", command=show_conclusion).pack()

# Start the game
start_game()

# Run the application
root.mainloop()
