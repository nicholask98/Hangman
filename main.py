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

word_list = ['despite', 'complex', 'project', 'rejected', 'adventure', 'hidden']

current_word = random.choice(word_list)

guess_count = 15

clear()
print('Welcome to Hangman! You have 15 guesses.\n')

correct_guesses = '_ ' * len(current_word)

for letter in current_word:
    print('_', end = ' ')
print()

user_letter = input('Enter a letter or "0" to quit:\n')
while user_letter != '0':
    guess_count -= 1
    if len(user_letter) == 1 and guess_count > 0:
        if user_letter in current_word:
            print(user_letter, 'is in the word.')
            # for letter in current_word:
            #     if letter == user_letter:    #FIXME: NOT SURE HOW TO DO THIS
            #         current_word[letter] = user_letter
        elif user_letter == '0':
            break
        else:
            print(user_letter, 'is not in the word.')
        sleep(1)
        clear()

        print(correct_guesses)
        user_letter = input('Enter a letter or "0" to quit:\n')
    elif user_letter.upper() == current_word.upper():
        print('You win!')
        break
    elif guess_count == 0:
        print('You ran out of guesses. :(')
        break
    else:
        print('Please enter one character.')
        user_letter = input('Enter a letter or "0" to quit:\n')

print('The word was', current_word)
print('Thanks for playing!')