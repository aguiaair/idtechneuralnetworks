#%%
import random
import time
import numpy as np
import os
chars = "abcdefghijklmnopqrstuvwxyz"



hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']




print('''
      ___           ___           ___           ___           ___           ___           ___     
     /__/\         /  /\         /__/\         /  /\         /__/\         /  /\         /__/\    
     \  \:\       /  /::\        \  \:\       /  /:/_       |  |::\       /  /::\        \  \:\   
      \__\:\     /  /:/\:\        \  \:\     /  /:/ /\      |  |:|:\     /  /:/\:\        \  \:\  
  ___ /  /::\   /  /:/~/::\   _____\__\:\   /  /:/_/::\   __|__|:|\:\   /  /:/~/::\   _____\__\:\ 
 /__/\  /:/\:\ /__/:/ /:/\:\ /__/::::::::\ /__/:/__\/\:\ /__/::::| \:\ /__/:/ /:/\:\ /__/::::::::.
 \  \:\/:/__\/ \  \:\/:/__\/ \  \:\~~\~~\/ \  \:\ /~~/:/ \  \:\~~\__\/ \  \:\/:/__\/ \  \:\~~\~~\/
  \  \::/       \  \::/       \  \:\  ~~~   \  \:\  /:/   \  \:\        \  \::/       \  \:\  ~~~ 
   \  \:\        \  \:\        \  \:\        \  \:\/:/     \  \:\        \  \:\        \  \:\     
    \  \:\        \  \:\        \  \:\        \  \::/       \  \:\        \  \:\        \  \:\    
     \__\/         \__\/         \__\/         \__\/         \__\/         \__\/         \__\/    
''')


print('Booting up...')
print('Defining...')
if input('Do you want to use a different dictionary [Y/n] ') =='Y':
    import urllib.request
    print('''Expecting:
    A .TXT file extension
    A direct download link''')
    # Download the file from `url` and save it locally under `file_name`:
    urllib.request.urlretrieve(input('URL:'), 'dict.txt')
    print('Success! Attempting to open file!')

else:
    print('Downloading default dictionary from the web by dwyl from GitHub...')
    import urllib.request
    # Download the file from `url` and save it locally under `file_name`:
    urllib.request.urlretrieve('https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt', 'dict.txt')
    print('Success! Attempting to open file!')


#Defining random_line to choose a random line drom an unpecified file
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print('Done!')

print('Choosing a random word...')
word=random_line('dict.txt')
wlen=len(word)
cletters=list(word)
clettersi=[]
tries=0
print('Done!')
if input('Do you want to enable debugging? [Y/n] ') =='Y':
  debug = True
else:
  debug = False
input('To start game press any key!')
gamerunning=True
while gamerunning:
    print (hangman[tries])
    if debug :
      print('DEBUG MODE')
      print(word)
    current=input('Letter: ')
    if current in cletters and current not in clettersi:
        print ('Yay!')
        clettersi.append(current)   
        print('You have guessed the letters:')
        print(*clettersi)
    elif current in cletters and current in clettersi:
            wcount = word.count(current)
            icount = clettersi.count(current)
            if wcount != icount:
                print ('Yay!')
                clettersi.append(current)
                print('You have guessed the letters:')
                print(*clettersi)
                if len(clettersi) == wlen:
                  print ('You have all the letters, now try to guess the word!')
                  if input('Word: ') == word:
                      print('You have won!')
                      gamerunning=False
            else:
                print ('Nope!')
                print('You have guessed the letters:')
                print(*clettersi)
                if tries <=4:
                    tries=tries+1
                else:
                    gamerunning=False
                    print (hangman[tries])

    elif len(clettersi) == wlen:
        print ('You have all the letters, now try to guess the word!')
        if input('Word: ') == word:
            print('You have won!')
            gamerunning=False
    else:
        print ('Nope!')
        if tries <=4:
            tries=tries+1
        else:
            gamerunning=False
            print (hangman[tries])
    input('Click any key to continue!')
    os.system('clear')
    print('You have guessed the letters:')
    print(*clettersi)
