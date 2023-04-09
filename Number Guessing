import random

logo = '''
 _______               ___.                        
 \      \  __ __  _____\_ |__   ___________  ______
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \/  ___/
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/\___ \ 
\____|__  /____/|__|_|  /___  /\___  >__|  /____  >
        \/            \/    \/     \/           \/ 
'''

def attempts():
  global initialTries
  initialTries -= 1
  if initialTries == 0:
    print('You lost')
  else:
    print(f"You have {initialTries} attempts remaining to guess the number")

print(logo)
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
searchedNumber = random.randrange(101)
guessed = False
if diff == 'hard':
  initialTries = 5
elif diff == 'easy':
  initialTries = 10

while not guessed and initialTries > 0:
  guessedNumber = int(input('Make a guess: '))
  if guessedNumber > searchedNumber:
    print('Too high')
    attempts()
  elif guessedNumber < searchedNumber:
    print('Too low')
    attempts()
  elif guessedNumber == searchedNumber:
    print(f'You got it! The searched number was {guessedNumber}')
    guessed = True
