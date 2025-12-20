def printText(label, text):
    if text !="ваш текст!":
        label.config(text=f"Вы ввели: {text}")
    else:
        label.config(text="")
