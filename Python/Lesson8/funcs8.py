def Convert(metrics1, metrics2, value, result):
    if len(metrics1) == 0 or len(metrics2) == 0:
        result.config(text="Одна из метрик не выбрана")

    elif not value.isdigit():
        result.config(text="В строке есть нечисловое символы")
    
    elif metrics1 == "Миллиметры":
        if metrics2 == "Миллиметры":
            result.config(text="Результат: " + value)
        elif metrics2 == "Сантиметры":
            result.config(text="Результат: " + str(int(value) / 10))
        elif metrics2 == "Дециметры":
            result.config(text="Результат: " + str(int(value) / 100))            
        elif metrics2 == "Метры":
            result.config(text="Результат: " + str(int(value) / 1000))
        elif metrics2 == "Километры":
            result.config(text="Результат: " + str(int(value) / 1000000))
    elif metrics1 == "Сантиметры":
        if metrics2 == "Миллиметры":
            result.config(text="Результат: " + str(int(value) * 10))
        elif metrics2 == "Сантиметры":
            result.config(text="Результат: " + value)
        elif metrics2 == "Дециметры":
            result.config(text="Результат: " + str(int(value) / 10))            
        elif metrics2 == "Метры":
            result.config(text="Результат: " + str(int(value) / 100))
        elif metrics2 == "Километры":
            result.config(text="Результат: " + str(int(value) / 100000))
    elif metrics1 == "Дециметры":
        if metrics2 == "Миллиметры":
            result.config(text="Результат: " + str(int(value) * 100))
        elif metrics2 == "Сантиметры":
            result.config(text="Результат: " + str(int(value) * 10))
        elif metrics2 == "Дециметры":
            result.config(text="Результат: " + value)           
        elif metrics2 == "Метры":
            result.config(text="Результат: " + str(int(value) / 10))
        elif metrics2 == "Километры":
            result.config(text="Результат: " + str(int(value) / 10000))
    elif metrics1 == "Метры":
        if metrics2 == "Миллиметры":
            result.config(text="Результат: " + str(int(value) * 1000))
        elif metrics2 == "Сантиметры":
            result.config(text="Результат: " + str(int(value) * 100))
        elif metrics2 == "Дециметры":
            result.config(text="Результат: " + str(int(value) * 10))            
        elif metrics2 == "Метры":
            result.config(text="Результат: " + value)
        elif metrics2 == "Километры":
            result.config(text="Результат: " + str(int(value) / 1000))
    elif metrics1 == "Километры":
        if metrics2 == "Миллиметры":
            result.config(text="Результат: " + str(int(value) * 1000000))
        elif metrics2 == "Сантиметры":
            result.config(text="Результат: " + str(int(value) * 100000))
        elif metrics2 == "Дециметры":
            result.config(text="Результат: " + str(int(value) * 10000))            
        elif metrics2 == "Метры":
            result.config(text="Результат: " + str(int(value) * 1000))
        elif metrics2 == "Километры":
            result.config(text="Результат: " + value)
        

