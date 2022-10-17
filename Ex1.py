# Задайте список из нескольких чисел. Напишите программу,
#  которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

########### Задача 1.1 (Напишите программу,которая посчитает сумму элементов,стоящих на нечетных индексах)
# a = input('Введите список: ').split()
# print(a)
# sum = 0
# b = a[1::2]
# for i in b:
#     sum += int(i)
# print (sum)

########### Задача 1.2
# a = list(map(int,input().split()))
# print(sum(list(filter(lambda i: i%2!=0,a))))

########### Задача 2.1(# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.)
# import math
# n = int(input('Введите число N = '))
# mass = []
# for i in range(1, n+1):
#     mass.append(math.factorial(i))
# print(mass)

############ Задача 2.2 ######################
# import math
# print(list(math.factorial(i) for i in range(1,int(input('Введите число N = '))+1)))

############ Задача 3.1(Задайте список из n чисел последовательности (1+1/n)^n )
# n = int(input('Введите число N = '))
# list = []
# for i in range(1, n+1):
#     list.append((1+1/i)**i)
# print(list)

############ Задача 3.2 
# li = [i for i in range(1,int(input('Введите число N = '))+1)]
# print(list(map(lambda i:(1+1/i)**i, li)))

############ Задача 4.1 ( Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
#  Элементы нужно выводить в том порядке, в котором они встречаются в списке.)
# import random
# a = [random.randint(-10,10) for i in range(10)]
# print (a)
# mass = []
# for i in a:
#     if a.count(i)==1:
#         mass.append(i)
# print ()
# print (mass)

############ Задача 4.2
# import random
# a = list(map(int,input().split()))
# print(list(filter(lambda i: a.count(i)==1,a)))
