# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
# for i in fruits:
#     count = 1
#     print(f"{count}.", '{}'.format(i).rjust(6))
#     count += 1

right_offset = len(max(fruits, key=len))

for index, item in enumerate(fruits, start=1):
    print('{}. {}'.format(index, item.rjust(right_offset)))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
#

listOne = [1, 2, 3, 4, 5]
listTwo = [8, 7, 6, 5, 4]

newList = []
for i in listOne:
    if i not in listTwo:
        newList.append(i)
print(newList)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

randomList = [1, 2, 3, 5, 7, 8, 9, 11, 14, 12, 76, 45, 86, 99]
listNew = []
for i in randomList:
    if i % 2 == 0:
        newI = i / 4
        listNew.append(newI)
    else:
        updatedI = i * 2
        listNew.append(updatedI)
print(listNew)
