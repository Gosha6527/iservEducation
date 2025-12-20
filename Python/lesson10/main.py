from tkinter import *
from funcs import *

mainWindow = Tk()
width = 700
height = 400
screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()
x_offset = (screen_width - width) // 2
y_offset = (screen_height - height) // 2

mainWindow.geometry(f"{width}x{height}+{x_offset}+{y_offset}")
mainWindow.title("Викторина")
mainWindow.resizable(not(True), False)

info = Label(text="", font = ("Arial", 12), fg = "red")
info.place(anchor="center", relx= 0.5, rely=0.25)

quest = Label(text="", font=("Arial", 16))
quest.place(anchor="center", relx=0.5, rely=0.15)

buttons = []
for i in range(4):
    btn = Button(width=50, height=1, font=("Arial", 14))
    btn.config(command=lambda b=btn: choice(b, quest, buttons, info))
    btn.place(anchor="center", relx= 0.5, rely=0.4+0.15*i)
    buttons.append(btn)

generate_quest(quest, buttons)







mainWindow.mainloop()