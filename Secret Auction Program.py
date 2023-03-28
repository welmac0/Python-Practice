import os
namesnbids = {}

def showWinner():
  tempValue = 0
  for key in namesnbids:
    if namesnbids[key] > tempValue:
      tempValue = namesnbids[key]
      winner = key

  print(f'The winner is {winner} who bid with ${namesnbids[winner]}')

def addAuction():
  name = input("What's your name?: ")
  bid = int(input("What's your bid?: $"))
  namesnbids[name] = bid
  decision = input("Are there any other bidders? Type 'yes' or 'no'.")
  if decision == 'yes':
    os.system('clear')
    addAuction()
  if decision == 'no':
    showWinner()

print("Welcome to the secret auction program")
addAuction()
