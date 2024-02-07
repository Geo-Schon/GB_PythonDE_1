""" Високосный ли год"""

year = int(input("Введите год: "))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) and (year < 1582):
    print('Високосный год')
else:
    print('Обычный год')

""" Посчитайте сумму четных элементов от 1 до n, исключая кратные e """

n = int(input("Введите число n: "))
e = int(input("Введите число e: "))
i = 2
summa = 0
while i < n:
    if i % e:
        pass
    else:
        if i % 2 == 0:
            summa = summa + i
    i += 1
print(summa)

"""
Числа и манипуляции с ними
"""

num = int(input("Введите число: "))
limit_1 = 10
limit_2 = 100
limit_3 = 1000
if 0 < num < limit_3:
    if num < limit_1:
        print(f"{num ** 2}")
    elif limit_1 <= num < limit_2:
        print(f"{(num % 10) + (num // 10)}")
    elif limit_2 <= num < limit_3:
        print(f"{(num % 10)}{(num//10 % 10)}{(num // 100)}")
else:
    print('Не подходит! Задайте новое число')

"""
Елочка
"""

rows = int(input("Введите количество рядов: "))
for i in range(rows):
    print(' '*(rows-i-1) + '*'*(2*i+1))

"""
Таблица умножения
"""

for i in range(2, 11):
    for j in range(1, 6):
        print(f"{i} * {j} = {i * j}", end="\t")
    print()
print()

for i in range(2, 11):
    for j in range(6, 11):
        print(f"{i} * {j} = {i * j}", end="\t")
    print()

