from tkinter import *
from tkinter import messagebox

class App:

    def __init__(self):
        self.__window = Tk()
        self.__window_width = 400
        self.__window_height = 500
        self.__screen_width = self.__window.winfo_screenwidth()
        self.__screen_height = self.__window.winfo_screenheight()
        self.__x = (self.__screen_width // 2) - (self.__window_width // 2)
        self.__y = (self.__screen_height // 2) - (self.__window_height // 2)
        self._name_app = "МойБанк"  
    
    def clear_form(self):
        for widget in self.__window.winfo_children():
            widget.destroy()

    def start_form(self):
        self.clear_form()
        authorization_button = Button(self.__window, text="Авторизация", width=20, font=("Arial", 16))
        authorization_button.place(anchor="center", relx=0.5, rely=0.3)

        registration_button = Button(self.__window, text="Регистрация", width=20, font=("Arial", 16),
                                     command=self.registration_form)   
        registration_button.place(anchor="center", relx=0.5, rely=0.4)

    def registration_form(self):
        self.clear_form()

        name_label = Label(self.__window, text="Имя пользователя", font=("Arial", 16))
        name_label.place(anchor="center", relx=0.5, rely=0.05)
        name_entry = Entry(self.__window, width=20, font=("Arial", 16))
        name_entry.place(anchor="center", relx=0.5, rely=0.15)

        phone_label = Label(self.__window, text="Номер телефона", font=("Arial", 16))
        phone_label.place(anchor="center", relx=0.5, rely=0.25)
        phone_entry = Entry(self.__window, width=20, font=("Arial", 16))
        phone_entry.place(anchor="center", relx=0.5, rely=0.35)

        password_label = Label(self.__window, text="Пароль", font=("Arial", 16))
        password_label.place(anchor="center", relx=0.5, rely=0.45)
        password_entry = Entry(self.__window, width=20, font=("Arial", 16))
        password_entry.place(anchor="center", relx=0.5, rely=0.55)

        repeat_password_label = Label(self.__window, text="Повторите пароль", font=("Arial", 16))
        repeat_password_label.place(anchor="center", relx=0.5, rely=0.65)
        repeat_password_entry = Entry(self.__window, width=20, font=("Arial", 16))
        repeat_password_entry.place(anchor="center", relx=0.5, rely=0.75)

        registration_complite = Button(self.__window, text="Зарегистрироваться", width=20, font=("Arial", 16))
        registration_complite.place(anchor="center", relx=0.5, rely=0.90)

    def start(self):   
        self.__window.geometry(f"{self.__window_width}x{self.__window_height}+{self.__x}+{self.__y}")
        self.__window.resizable(False, False)
        self.__window.title(self._name_app)

        self.start_form()
        
        self.__window.mainloop()