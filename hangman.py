#!/usr/bin/env python3
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

endofgame = False
wordlist = ["tray,", "complication", "establish", "module", "jungle"]
chosenword = random.choice(wordlist)
wordlength = len(chosenword)

lives = 6
display = []

for _ in range(wordlength):
    display += "_"

while not endofgame:
    guess = input("Guess a letter: ").lower()

    for position in range(wordlength):
        letter = chosenword[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter


    if guess not in chosenword:
        lives -= 1
        if lives == 0:
            endofgame = True
            print("You lose")

    print(f"{' '.join(display)}")
#print(display)


    if "_" not in display:
        endofgame = True
        print("You win.")

    print(stages[lives])