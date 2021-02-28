import random

from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

word_list = ['despite', 'complex', 'project', 'rejected', 'adventure', 
'hidden', 'vacuum', 'friends', 'seniors', 'blanket', 'window', 'deadly',
'secret', 'horrible', 'contemporary', 'abrasive', 'orange', 'watermelon',
'curtain', 'dresser', 'cousin', 'cushion', 'family', 'convertible', 'pillow',
'sanctum', 'heaven', 'driving', 'automobile', 'relaxing']

play_again = 'y'
while play_again == 'y':
    current_word = random.choice(word_list)

    guess_count = 13

    clear()
    print('Welcome to Hangman! You have 13 guesses.\n')

    correct_guesses = '-' * len(current_word)
    incorrect_guesses = []
    print(correct_guesses.upper())
    user_letter = input('Enter a letter, take a full guess at the word, or "0" to quit:\n')
    

    while user_letter != '0':
        clear()
        
        while user_letter.isdigit() or not(user_letter.isalnum()):
            print("invalid entry.")
            sleep(.5)
            clear()
            print('Guesses Left: {}'.format(guess_count))
            print(correct_guesses.upper())
            print('Incorrect guesses: {}'.format(incorrect_guesses))
            user_letter = input('Enter a letter, take a full guess at the word, or "0" to quit:\n')
            if user_letter == '0':
                break
            continue
        if user_letter == '0':
            break
        user_letter = user_letter.lower()
        
        if user_letter.lower() == current_word.lower():
            print('You Win!')
            break

        if len(user_letter.lower()) > 1:
            guess_count -= 1

        if len(user_letter) == 1:
            guess_count -= 1
            if user_letter in current_word:
                num_occurances = current_word.count(user_letter)
                current_index = 0
                for letter in range(num_occurances):
                    if current_word.find(user_letter) != 0:
                        current_index = current_word.find(user_letter, current_index + 1)
                    correct_guesses = correct_guesses[:current_index] + user_letter + correct_guesses[current_index + 1:]
            elif user_letter not in current_word:
                incorrect_guesses.append(user_letter)
        
        if len(user_letter) == 0:
            print('invalid entry')
            sleep(.5)
            clear()
            print('Guesses Left: {}'.format(guess_count))
            print(correct_guesses.upper())
            print('Incorrect guesses: {}'.format(incorrect_guesses))
            user_letter = input('Enter a letter, take a full guess at the word, or "0" to quit:\n')
            clear()
            continue
        if guess_count == 0:
            print(correct_guesses.upper())
            print('Incorrect guesses: {}'.format(incorrect_guesses))
            print('You lose!')
            break
        elif correct_guesses.find('-') == -1:
            print('You Win!')
            break
        clear()
        print('Guesses Left: {}'.format(guess_count))
        print(correct_guesses.upper())
        print('Incorrect guesses: {}'.format(incorrect_guesses))
        user_letter = input('Enter a letter, take a full guess at the word, or "0" to quit:\n')


    print('The word was', current_word)
    play_again = 'n'
    if user_letter != '0':
        play_again = input('enter [y] to play again. Press anything else to quit.\n')
print('Thanks for playing!')