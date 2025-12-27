class Car:
    def __init__(self, name, color, power):
        self.name = name
        self.color = color
        self.power = power
        self.mileage = 0
        self.isRunning = False
    
    def startEngine(self):
        if self.isRunning:
            print("Двигатель уже запущен")
            return
        self.isRunning = True
        print("Двигатель запущен")

    def stopEngine(self):
        if not(self.isRunning):
            print("Двигатель не запущен")
            return
        self.isRunning = False
        print("Двигатель заглушен")

    

    def printInfo(self):
        print("10*=")
        print(f"Название машины: {self.name}")
        print(f"Цвет: {self.color}")
        print(f"Мощность: {self.power}")
        print("10*=")

class Cat:
    def __init__(self, poroda, color, name, weight):
        self.name = name
        self.color = color
        self.poroda = poroda
        self.weight = weight
        self.sleep = False

    def razbudit(self):
        if not(self.sleep):
            print("Кошка не спит вы не можете её разбудить")
        else: 
            print("Кошка больше не проснётся, вы её усыпили")
    
    def usipit(self):
        if self.sleep:
            print("Вы уже усыпили кошку")
        else:
            self.sleep = True
            print("Вы усыпили кошку")

    def printMiau(self):
        print("Мяу")
    
    def feed(self, skolko):
        if self.sleep:
            print("Вы усыпили кошку и не можете её покормить")
            return
        if (skolko < 0):
            print("вы достали корм из кошки")
        else:
            print("Вы покормили кошку")
        self.weight += skolko
        print(f"Сейчас кошка весит {self.weight} кг")