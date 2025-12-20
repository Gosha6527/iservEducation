from Python.Lesson8.funcs8 import *
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("!Первое приложение")
root.geometry("500x300")

text1 = ttk.Label(text = "Из")
text1.place(relx = 0.1, rely = 0.11)

metrics = ["Миллиметры", "Сантиметры", "Дециметры", "Метры", "Километры"]

items1 = ttk.Combobox(values = metrics)
items1.place(relx=0.15, rely=0.1, width=150, height=30)

text2 = ttk.Label(text = "в")
text2.place(relx = 0.5, rely = 0.11)

items2 = ttk.Combobox(values = metrics)
items2.place(relx=0.55, rely=0.1, width=150, height=30)

text3 = ttk.Label(text="Введите значение:")
text3.place(relx=0.15, rely=0.3)

inputNum = ttk.Entry()
inputNum.place(relx=0.15, rely=0.4, width=150, height=30)

result = ttk.Label(text = f"Результат: {0}")
result.place(relx=0.55, rely=0.4)

convert = ttk.Button(text = "Конвертировать", command=lambda: Convert(items1.get(), items2.get(), inputNum.get(), result))
convert.place(relx=0.35, rely=0.6, width=150, height=50)

























root.mainloop()