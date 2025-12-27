from car import *
car1 = Car("Lada Granta", "Чёрный", 200)
car2 = Car("Kia K5", "Белый", 500)
cat = Cat("Британская", "Рыжий", "Кот", 12)

car2.color = 53
'''
print(getattr(car1, "name"))
car1.startEngine()
car1.startEngine()
car1.stopEngine()
car1.stopEngine()
car1.printInfo()
car2.printInfo()
'''

cat.feed(234)
cat.feed(-36)
cat.razbudit()
cat.razbudit()
cat.usipit()
cat.usipit()
cat.razbudit()
cat.feed(23)