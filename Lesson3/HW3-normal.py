# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.


def salary_def(dictionary):
    """
    :dictionary: передаём в функцию словарь
    :return: возвращает словарь, в который не попали сотрудники с ЗП более 6000
    """
    new_data = dictionary.copy()
    for key, value in new_data.items():
        if value > 6000:
            del dictionary[key]
    return dict


name = ['Alex', 'John', 'Sean', 'Robert']
salary = [1000, 3000, 5000, 7000]

data = dict(list(zip(name, salary)))

with open('salary.txt', 'w', encoding='utf-8') as file:
    salary_def(data)
    for key, value in data.items():
        file.write('{} - {}\n'.format(key.upper(), value))
