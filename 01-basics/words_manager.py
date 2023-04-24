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

    def user_input(self):
        while True:
            word = input("enter a word: ")
            if type(word) != str or len(word) != 5:
                print("Invalid input")
                continue
            else:
                return word.lower()

