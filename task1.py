length = float(input("Введите длину прямоугольника: "))
width = float(input("Введите ширину прямоугольника: "))

if length <= 0 or width <= 0:
    print("Некорректные значения длины и ширины")
else:
    print(f"Периметр: {length * 2 + width * 2}. Площадь: {length * width}")