from utils import load_random_word, print_rezults
from classes import Player


def main():
    file_name = 'https://api.npoint.io/6cf56e4d3c5307359b20'
    basic_word = load_random_word(file_name)

    user_name = input('Введите имя игрока: ').title()
    player1 = Player(user_name)

    print(f'Привет, {player1.user_name}!')
    print(f'Составьте {basic_word.count_words()} слов из слова {basic_word.word.upper()}')
    print('Слова должны быть не короче 3 букв.\nЧтобы закончить игру, угадайте все слова или напишите "stop".')
    print('Поехали, ваше первое слово?')

    flag = True

    while (basic_word.count_words() != len(player1.list_used_words)) and flag:
        user_word = input('>').lower()
        if len(user_word) < 3:
            print('Слишком короткое слово!')
            user_word = input('>').lower()

        if user_word == 'stop' or user_word == 'стоп':
            flag = False
            print_rezults(player1.count_used_words() - 1)

        if basic_word.check_word(user_word):
            if player1.check_word_before(user_word):
                print('Уже использовано!')
            else:
                print('Верно!')
                player1.used_words(user_word)
                player1.count_used_words()
        else:
            if flag:
                print('Неверно!')

    if basic_word.count_words() == len(player1.list_used_words):
        print_rezults(player1.count_used_words() - 1)

if __name__ == '__main__':
    main()
