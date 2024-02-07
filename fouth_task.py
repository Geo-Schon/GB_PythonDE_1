"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать “больше”
 или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
"""

from random import randint

guess = randint(0, 1000)
guessed = False
attempts = 0
left = 0
right = 1001

while not guessed:
    mid = (left + right) // 2
    print(mid)
    answer = input(f"Ваше число равно, больше или меньше {mid}? Введите '=', '>', или '<'): ")
    if not answer in ("<", ">", "="):
        print("Так нельзя! Введите '=', '>', или '<'")
        continue
    if answer == "<":
        right = mid
    elif answer == ">":
        left = mid
    else:
        guessed = True
    attempts += 1
    print(f"Это {attempts} попытка")
print(f"Отлично! Загаданное число {mid}. Отгадано за {attempts} попыток")
