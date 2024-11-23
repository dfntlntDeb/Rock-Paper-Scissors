import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import random as rnd

def rps_play():
    player = player_choice.get()  # Get the player's choice
    computer = rnd.choice(choices)  # Randomly select computer's choice

    # Update images based on choices
    player_choice_img.config(image=player_img[player])
    computer_choice_img.config(image=computer_img[computer])

    # Winner Checker and Result Printer
    if player == computer:
        result_label.config(text="It's a tie!")
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        result_label.config(text="Player wins!")
    else:
        result_label.config(text="Computer wins!")

gamewindow = tk.Tk()
gamewindow.title("Rock Paper Scissors")
gamewindow.geometry("700x350")
gamewindow.maxsize(700,350)

# Player choice
choices = ["rock", "paper", "scissors"]
player_choice = tk.StringVar(value=choices[0])

player_img = {
    "rock": ImageTk.PhotoImage(Image.open("imgs/bluerock.png").resize((150, 150))),
    "paper": ImageTk.PhotoImage(Image.open("imgs/bluepaper.png").resize((150, 150))),
    "scissors": ImageTk.PhotoImage(Image.open("imgs/bluescissors.png").resize((150, 150)))
}

computer_img = {
    "rock": ImageTk.PhotoImage(Image.open("imgs/redrock.png").resize((150, 150))),
    "paper": ImageTk.PhotoImage(Image.open("imgs/redpaper.png").resize((150, 150))),
    "scissors": ImageTk.PhotoImage(Image.open("imgs/redscissors.png").resize((150, 150)))
}

# Header frame
header = tk.Frame(gamewindow, height=100)
header.grid(column=0, row=0, columnspan=3, sticky="ew")

header.grid_columnconfigure(0, weight=1)
header.grid_columnconfigure(1, weight=1)
header.grid_columnconfigure(2, weight=1)

# Labels
player = tk.Label(header, text="Player", font=("Arial", 30, "bold"), anchor="e")
player.grid(column=0, row=0, padx=(20, 0), pady=(20, 0), sticky="e")

vs = tk.Label(header, text="", font=("Arial", 30, "bold"))
vs.grid(column=1, row=0, pady=(20, 0), sticky="nsew", padx=167)

computer = tk.Label(header, text="Computer", font=("Arial", 30, "bold"), anchor="w")
computer.grid(column=2, row=0, padx=(0, 20), pady=(20, 0), sticky="w")

# Image frame
img_frame = tk.Frame(gamewindow, width=100)
img_frame.grid(column=0, row=1, columnspan=3, sticky="ew")

img_frame.grid_columnconfigure(0, weight=1)
img_frame.grid_columnconfigure(1, weight=1)
img_frame.grid_columnconfigure(2, weight=1)

# Player choice image
player_choice_img = tk.Label(
    img_frame,
    image=player_img[choices[0]],
    anchor="center"
)
player_choice_img.grid(
    column=0,
    row=0,
    rowspan=2,
    pady=(20, 0),
    padx=(20, 0),
    sticky="e"
)

versus = tk.Label(
    img_frame,
    text="VS",
    font=("Arial", 30, "bold"),
    width=5,
    anchor="center"
)
versus.grid(
    column=1,
    row=0,
    rowspan=2,
    pady=(20, 0),
    padx=110,
    sticky="nsew"
)

# Computer choice image
computer_choice_img = tk.Label(
    img_frame, 
    image=computer_img[choices[0]], 
    anchor="e"
    )

computer_choice_img.grid(
    column=2, 
    row=0, 
    rowspan=2, 
    pady=(20, 0), 
    padx=(0, 20), 
    sticky="w"
    )

# Final frame
final = tk.Frame(
    gamewindow, 
    width=100
    )

final.grid(
    column=0, 
    row=2, 
    columnspan=3, 
    sticky="ew"
    )

final.grid_columnconfigure(0, weight=1)
final.grid_columnconfigure(1, weight=1)
final.grid_columnconfigure(2, weight=1)

# Dropdown for player choice
player_drpdwn = ttk.Combobox(
    final, 
    textvariable=player_choice, 
    values=choices, 
    state="readonly"
    )

player_drpdwn.grid(
    row=0, 
    column=0, 
    sticky="e"
    )

# Play button
play_btn = tk.Button(
    final,
    text="Play",
    command=rps_play
    )

play_btn.grid(
    row=0,
    column=1,
    padx=(20, 0),
    pady=(20, 0)
    )

# Result label
result_label = tk.Label(
    final,
    text="",
    font=("Arial", 25, "bold"),
    width=20,  # Set a fixed width to prevent resizing
    anchor="center"  # Center the text within the label
)
result_label.grid(
    row=0,
    column=2,
    padx=(0, 20),
    pady=(20, 0)
    )

gamewindow.mainloop()
