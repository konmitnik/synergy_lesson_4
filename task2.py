num = int(input("Введите пятизначное число: "))
ten_thousand = int(num / 10000)
num %= 10000
thousand = int(num / 1000)
num %= 1000
hundred = int(num / 100)
num %= 100
ten = int(num / 10)
unit = num % 10

print((ten ** unit) * hundred / (ten_thousand - thousand))