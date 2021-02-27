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

for letter in current_word:
    print('_', end = ' ')
print()

user_letter = ''
while user_letter != '0':
    user_letter = input('Enter a letter or "0" to quit:\n')
    if user_letter in current_word:
        print(user_letter, 'is in the word.')
    elif user_letter == '0':
        break
    else:
        print(user_letter, 'is not in the word.')
    sleep(1)
    clear()

print('The word was', current_word)
print('Thanks for playing!')