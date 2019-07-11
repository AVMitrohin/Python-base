import math, random

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

# list = []
# # list = [random.randint(0, 100) for i in range (5)]
# newList = []
# qntNumber = int(input('Введите число больше 0: '))
#
# while len(list) < qntNumber:
#     i = random.randint(0, 100)
#     list.append(i)
# for value in list:
#     newValue = value ** 2
#     newList.append(newValue)
#
# print(list)
# print(newList)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# firstFruits = ['apple', 'banana', 'orange', 'kiwi']
# secondFruits = ['strawberry', 'kiwi', 'tangerine', 'apple']
#
# list = []
#
# for fruit in firstFruits:
#     if fruit in secondFruits:
#         list.append(fruit)
#
# print(list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

list = [random.randint(-100, 100) for i in range(random.randint(0, 10))]
listNew = []

for i in list:
    if i % 3 == 0 and i > 0:
        listNew.append(i)
    elif i % 4 != 0 and i > 0:
        listNew.append(i)

print(listNew)


