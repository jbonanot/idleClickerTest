import tkinter as tk 
from tkinter import ttk
from tkinter import *

scoreValue = 0

def scoreUp():
    global scoreBox
    global scoreValue
    scoreValue = scoreValue + 1
    scoreBox["text"] = "Score: " + str(scoreValue)

window = tk.Tk()
window.geometry('700x700')
window.resizable(False, False)
window.title('Idle Clicker')
window.configure(bg='black')

main_button = ttk.Button(
    window,
    text="Click me!",
    command = scoreUp
)

scoreBox = Label(
    window, 
    text="Score: " + str(scoreValue)
)

main_button.pack(
    ipadx=20,
    ipady=20,
    expand=True
)
scoreBox.pack(
    ipadx=30,
    ipady=15,
)

window.mainloop()
