import math, random

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

listOne = [9, -5, 8, 121, -25, 25, 4]
newList = []

for i in listOne:
    if i > 0 and math.sqrt(i).is_integer():
        newList.append(int(math.sqrt(i)))
    elif i < 0:
        pass
print(newList)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date = '19.01.2018'
day = {'01': 'Первое', '02': 'Второе', '03': 'Третье', '04': 'Четвертое', '05': 'Пятое', '06': 'Шестое',
       '07': 'Седьмое',
       '08': 'Восьмое', '09': 'Девятое', '10': 'Десятое', '11': 'Одиннадцатое', '12': 'Двенадцатое',
       '13': 'Тринадцатое',
       '14': 'Четырнадцатое', '15': 'Пятнадцатое', '16': 'Шестнадцатое', '17': 'Семьнадцатое', '18': 'Восемнадцатое',
       '19': 'Девятнадцатое', '20': 'Двадцатое'}
month = {'01': 'Января', '02': 'Февраля', '03': 'Марта', '04': 'Апреля', '05': 'Мая', '06': 'Июня', '07': 'Июля',
         '08': 'Августа', '09': 'Сентября', '10': 'Октября', '11': 'Ноября', '12': 'Декабря'}
year = {'2010': '2010 года', '2011': '2011 года', '2012': '2012 года', '2013': '2013 года', '2014': '2014 года',
        '2015': '2015 года', '2016': '2016 года', '2017': '2017 года', '2018': '2018 года', '2019': '2019 года'}

new = date.split('.')
print(day[new[0]], month[new[1]], year[new[2]])

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

randomList = []
cntNumber = int(input('Введите произвольное положительное число: '))
while len(randomList) < cntNumber:
    i = random.randint(-100, 100)
    randomList.append(i)
print(randomList)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = set(lst)
print(lst2)
lst3 = [1, 2, 4, 5, 6, 2, 5, 2]
lst4 = []
for i in lst3:
    if lst3.count(i) == 1:
        lst4.append(i)
print(lst4)


