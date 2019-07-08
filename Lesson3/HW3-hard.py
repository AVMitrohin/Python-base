# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


def attack(player1, player2):
    damage = player1['damage']
    health = player2['health']
    new_health = health - damage
    player2.update({'health': new_health})
    print(f"Игрок {player2['name']} получил {damage} урона. У него осталось {new_health} здоровья")


playerName = str(input('Введите имя первого игрока: '))
enemyName = str(input('Введите имя второго игрока: '))

player = {'name': playerName, 'health': 100, 'damage': 40}
enemy = {'name': enemyName, 'health': 130, 'damage': 60}

attack(enemy, player)
