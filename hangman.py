import random

isWin = False
winPoints = 0
lostPoints = 0
from words import word_list as wordList
from words import logo
chosenWord = random.choice(wordList)
display = []

for j in range(0, len(chosenWord)):
  display += '_'
print(logo)
print(*display, sep=' ')

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

while isWin == False:
  tempLife = winPoints
  guess = input('Guess a letter: ').lower()
  for i in range(0, len(chosenWord)):
    if guess == chosenWord[i]:
      #print('right')
      display[i] = guess
      winPoints += 1
      if winPoints == len(chosenWord):
        isWin = True
        print('You won!')
    else:
      pass
  else:
    if tempLife == winPoints:
      lostPoints += 1
      print(f'{guess} is not a letter')
      print(f"You've lost a life, lifes to end: {len(chosenWord) - lostPoints}")
      print(stages[len(chosenWord) - lostPoints])
      if lostPoints == len(chosenWord):
        isWin = True
        print('You lost! The word was:')
        print(*chosenWord, sep =' ')
    if isWin == False:
      print(*display, sep=' ')
