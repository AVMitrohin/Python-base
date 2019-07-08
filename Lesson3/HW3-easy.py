# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"


def personal_info(name, age, city):
    return (f'{name}, {age} год(а), проживает в городе {city}')


name = input('Напишите ваше имя: ')
age = input('Сколько вам лет? ')
city = input('В каком городе вы живёте? ')
print((personal_info(name, age, city)))

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них


def find_max(firstNumber, secondNumber, thirdNumber):
    return max(firstNumber, secondNumber, thirdNumber)


answer = find_max(1, 4, 3)
print(answer)

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def max_str(*args):
    return max(*args, key=len)


maxStr = max_str('aa', 'zzz', 't')
print(maxStr)
