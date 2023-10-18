import random
import words_fetcher

words = words_fetcher.fetch_words(min_letters=5, max_letters=5)
computer_word = random.choice(words)
# print('DEBUG', computer_word)

try_count = 1

while True:
    user_word = input(f'Enter a word (try {try_count} out of 6): ').lower()
    if user_word not in words:
        print('The word is not in the dictionary, try again')
        continue

    if user_word == computer_word:
        print('You won! The word is indeed', user_word)
        break

    try_count = try_count + 1

    for i in range(len(user_word)):
        user_letter = user_word[i]
        computer_letter = computer_word[i]
        if user_letter == computer_letter:
            print(user_letter.upper(), end=' ')
        elif user_letter in computer_word:
            print(user_letter, '*', sep='', end=' ')
        else:
            print(user_letter, end=' ')
    print()

    if try_count == 7:
        print('You lose! The word is', computer_word)
        break
