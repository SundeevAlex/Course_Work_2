import requests, random
from classes import BasicWord


def load_random_word(file_name):
    response = requests.get(file_name)
    data = response.json()
    random.shuffle(data)
    data_one = data[0]
    basic_word = BasicWord(data_one["word"], data_one["subwords"])
    return basic_word


def print_rezults(count):
    print(f'Игра завершена, вы угадали {count} слов(а)!')
