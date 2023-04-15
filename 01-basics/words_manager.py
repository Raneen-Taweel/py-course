import random
import words as data

class WordsManager:
    def __init__(self):
        self.words = data.words_5_letters

    def select_random_word(self):
        return random.choice(self.words)

    def check_word(self, word):
       if word in data.words_5_letters:
           return True