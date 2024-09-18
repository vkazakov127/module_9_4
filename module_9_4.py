# -*- coding: utf-8 -*-
# module_9_4.py
print("---------------- lambda-функция ----------")
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(f'first="{first}", \nsecond="{second}"')
print(f'result= {result}')
print("------------------- Замыкание ------------")


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, mode='a', encoding='utf8') as file:
            for item in data_set:
                file.write(str(item) + "\n")
        return file.closed

    return write_everything


example_file_name = 'example.txt'
write = get_advanced_writer(example_file_name)
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
print(f'Покажем, что записалось в файл "{example_file_name}": ')
with open(example_file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line, end='')
print(f'file.closed: {file.closed}')
print("----------------- Метод __call__ ---------")

from random import choice


class MysticBall:
    def __init__(self, *args):
        self.words = [*args]

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())

print('------------ The End ----------')
