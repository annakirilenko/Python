# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 2 4 8

n = int(input("Введите число N: "))
m = 1
while m < n:
    if (m * 2 > n):
            break
    else:
        m = m * 2
        print(m)