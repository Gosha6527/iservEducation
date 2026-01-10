from animals import *

def info(object):
    object.printInfo()

def animalSpeak(object):
    object.speak()


cat = Cat("Гав", 3, "Бенгальская")
dog = Dog("Бобик", 5, "Хаски")
newCat = HomeCat("Муся", 4, "Сибирская", "Рыжая", "Вова")

newCat.printInfo()
info(newCat)
info(cat)
info(dog)
animalSpeak(cat)
animalSpeak(newCat)
animalSpeak(dog)
