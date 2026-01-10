class Cat:
    def __init__(self, name, age, poroda):
        self.__name = name
        self.__age = age
        self.__poroda = poroda

    def printInfo(self):
        print("Информация о кошке")
        print(f"Имя: {self.__name}")
        print(f"Возраст: {self.__age}")
        print(f"Порода: {self.__poroda}")

    def speak(self):
        print("Кошка говорит Мяу!")

class HomeCat(Cat):
    def __init__(self, name, age, poroda, color, owner):
        super().__init__(name, age, poroda)
        self.__color = color
        self.__owner = owner
        self.__is_sleep = False
    
    def printInfo(self):
        super().printInfo()
        print(f"Цвет: {self.__color}")
        print(f"Хозяин: {self.__owner}")

    def play(self):
        if self.__is_sleep:
            print("Кошкка спид и не может играть.")
            return
        print("Кошка начала играть")


class Dog:
    def __init__(self, name, age, poroda):
        self.__name = name
        self.__age = age
        self.__poroda = poroda

    def printInfo(self):
        print("Информация о собаке")
        print(f"Имя: {self.__name}")
        print(f"Возраст: {self.__age}")
        print(f"Порода: {self.__poroda}")

    def speak(self):
        print("Кошка говорит Гав!")