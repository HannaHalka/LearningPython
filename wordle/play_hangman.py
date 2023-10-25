import random
import words_fetcher

words = words_fetcher.fetch_words(min_letters=6, max_letters=20)
computer_word = random.choice(words)
print('DEBUG', computer_word)

print('the word is', end=' ')
print("." * len(computer_word))


mistake_count = 1
guessed_letters = []

while True:
    user_letter = input('please enter one letter ')

    if user_letter in computer_word:
        guessed_letters.append(user_letter)
        user_won = True
        for letter in computer_word:
            if letter in guessed_letters:
                print(letter, end='')
            else:
                user_won = False
                print('.', end='')
        print()  # line break
        if user_won:
            print(f'You won! The word is {computer_word}')
            break
        else:
            continue

    print(f'No such letter, {mistake_count} / 8 mistakes')
    mistake_count += 1
    if mistake_count > 8:
        print('You lose! The word is', computer_word)
        break
