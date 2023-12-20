class BasicWord:
    def __init__(self, word, words, user_word=None):
        self.word = word
        self.words = words


    def check_word(self, user_word):
        """
        проверка введенного слова в списке допустимых подслов
        """
        self.user_word = user_word
        if self.user_word in self.words:
            return True
        return False


    def count_words(self):
        """
        подсчет количества подслов
        """
        return len(self.words)


    def __repr__(self):
        return f"BasicWord: Слово: {self.word}. Подслова: {self.words}. Кол-во слов: {len(self.words)}"


class Player:
    list_used_words = []
    count = 0

    def __init__(self, user_name, used_words_user=None):
        self.user_name = user_name
        self.used_words_user = used_words_user


    def count_used_words(self):
        """
        получение количества использованных слов
        """
        self.count += 1
        return self.count


    def used_words(self, used_words_user):
        """
        добавление слова в использованные слова
        """
        self.list_used_words.append(used_words_user)


    def check_word_before(self, user_word):
        """
        проверка использования данного слова до этого
        """
        self.user_word = user_word
        if self.user_word in self.list_used_words:
            return True
        return False


    def __repr__(self):
        return f"Player: Имя: {self.user_name}. Использованные слова: {self.list_used_words}. Кол-во угаданных слов: {self.count}"
