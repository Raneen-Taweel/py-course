from words_manager import WordsManager

w = WordsManager()
hidden_word = w.select_random_word()
attempt = 6

print(hidden_word)

while attempt > 0:
    print(f'You have {attempt} tries')
    guess_word = w.user_input()
    if hidden_word == guess_word:
        print("You guessed it!")
        break
    else:
        w.check_guess(hidden_word, guess_word)
        print('\n')

    attempt-= 1
    if attempt == 0:
        print(f'Sorry, You have used up your guesses! The word was: {hidden_word.upper()}')
