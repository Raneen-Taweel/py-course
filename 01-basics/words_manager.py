import random
import words as data

class WordsManager:
    def __init__(self):
        self.words = data.words_5_letters

    def select_random_word(self):
        return random.choice(self.words)

    """def check_word(self, word):
       if word in data.words_5_letters:
           return True"""

    def user_input(self):
        while True:
            word = input("Enter the word: ").lower()
            if type(word) != str or len(word) != 5:
                print("Invalid input! Enter a five letter word")
                continue
            if word not in data.words_5_letters:
                print("Invalid input! Enter a five letter word")
                continue
            else:
                return word.lower()

    def check_guess(self, hidden_word, guess_word):
        for correct_letter, letter in zip(hidden_word, guess_word):
            if letter == correct_letter:
                print(letter.upper(), end='')
            elif letter in hidden_word:
                print(letter.lower(), end='')
            else:
                print('-', end='')