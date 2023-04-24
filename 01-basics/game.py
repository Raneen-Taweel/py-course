from words_manager import WordsManager

w = WordsManager()
hidden_word = w.select_random_word()
attempt = 6

print(hidden_word)

while attempt > 0:
    print(attempt)
    guess_word = w.user_input()
    if w.check_word(guess_word):
        if hidden_word == guess_word:
            print("You guessed it!")
            break
        for correct_letter, letter in zip(hidden_word, guess_word):
            if letter == correct_letter:
                print(letter.upper(), end='')
            elif letter in hidden_word:
                print(letter.lower(), end='')
            else:
                print('-', end='')
        attempt-= 1