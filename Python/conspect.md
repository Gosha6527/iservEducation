# Мой конспект

### Темы
- **Условия**
- Ввод данных
- Циклы
- Типы данных

## Приложение для регистрации пользователя


```
print("Регистрация\n\n")
name = input("Введите имя: ")
age = int(input("Введите возраст: "))
isChild = False

if age < 18:
    isChild = True

login = input("Введите логин: ")
password = input("Введите пароль: ")
repeatPassword = input("Повтроите пароль: ")
while (password != repeatPassword):
    print("Пароли не совпадают!")
    repeatPassword = input("Повтроите пароль: ")

print("Успешная регистрация!")
```

## Программа определения возраста
```
year = 2025
month = 10
date = 25

birthYear = int(input("Введите ваш год рождения: "))
birthMonth = int(input("Введите ваш месяц рождения: "))
birthDate = int(input("Введите ваше число рождения: "))

age = year - birthYear

if(month < birthMonth):
    age-=1
elif(month == birthMonth):
    if(date < birthDate):
        age-=1

print(f"Ваш возраст {age} лет")
```
## Практика цикла While
```
proizv = 1
a = int(input())
proizv *= a
while a != 0:
    proizv *= a
    a = int(input())     
print(proizv)
```

## что это
```
for i in range(1, 101):
    if i%3 != 0 and i%5 != 0:
        print(i)
```

```
st = input(Текст:)
a = int(input())
while not(a < len(st)-1):
    a = int(input(A:))
b = int(input())
while not(a < b):
    b = int(input(B:))

print(st[a:b])
```

## Проверка на палиндром
```
while True:
    text = input("Введите палиндром: ")
    if text == text[::-1]:
        print("Верно")
    else:
        print("это не очень палиндром")
```

## Метод replace
```
text = input("Введите текст: ")
text = text.replace(".", "")
text = text.replace(",", "")
text = text.replace("!", "")
text = text.replace("?", "")
print(text)
```

## Списки
```
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(1, "lemon")
fruits.remove("banana")
print(fruits)
```


## Модуль math
```
import math

part_1_1 = math.cos(math.pi/3) + math.log2(16)
part_1_2 = sum([math.factorial(n) + 1 for n in range(0,4)])
part_1 = part_1_1 * part_1_2
part_2 = (math.sqrt(25) - abs(-5)) ** math.sin(math.pi/2)
part_3 = (3 ** 2 + 4 ** 2) / 5 * (math.tan(0) + 1)
result = part_1 + part_2 - part_3
print(result)
```

## Модуль random
```
import random as rand

life = 5 
rand_num = rand.randint(1,50)
isWin = False
while life != 0:
    num = int(input("Введите число: "))
    if num == rand_num:                                              
        print("Вы угадали")
        isWin = True
    elif num < rand_num:
        print("Загаданное число больше")
    elif num > rand_num:
        print("Загаданное число меньше")
    life -= 1
if not isWin:
    print("Вы проиграли :(")
```

## Turtle

```
import turtle

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("lightblue")
screen.title("Весёлый смайлик - изучаем Turtle")

t = turtle.Turtle()
t.speed(10)
t.width(3)
def drawCircle(x,y,color,rad):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("black", color)
    t.begin_fill()
    t.circle(rad)
    t.end_fill()

drawCircle(0,-100,"yellow",100)
drawCircle(-40,30,"white",20)
drawCircle(40,30,"white", 20)
drawCircle(-40, 40,"black",10)
drawCircle(40, 40,"black",10)

t.penup()
t.goto(-60, -20)
t.pendown()
t.color("black")
t.width(5)
t.setheading(-60)
t.circle(70,120)

screen.exitonclick()
```


## Функции
### Пароль
```
import random
import string

def password_generation(lenPas, isNums, isUpAlpha):
    symbols = string.ascii_lowercase
    password = ""
    if isUpAlpha:
        symbols += string.ascii_uppercase
    if isNums:
        symbols += "123456780"

    for _ in range(lenPas):
        password += random.choice(symbols)

    return password

print("Программа для генерации пароля")
lenPas = int(input("Введите длину пароля: "))
isNums = input("Нужны ли цифры в пароле? Y/n \n")
isUpAlpha = input("Нужны ли заглавные буквы? Y/n \n")

if isNums.lower() == "y":
    isNums = True
else:
    isNums = False

if isUpAlpha.lower() == "y":
    isUpAlpha = True
else:
    isUpAlpha = False

password = password_generation(lenPas, isNums, isUpAlpha)

print(password)
```

### другие ф-нции
```
import random
import string

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return not True

def howManyVowels(str):
    amountOfVowels = 0
    vowels = "аеёиуюэыюо"
    for i in vowels:
        amountOfVowels += str.count(i)
    return amountOfVowels
print(howManyVowels("гласные"))

def sumDigitsOfNums(num):
    result = 0
    for i in str(num):
        result += int(i)
    return result
```