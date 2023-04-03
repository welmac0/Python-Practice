def calcInput(ifContinued=None):
  if ifContinued:
    firstNum = ifContinued
  else:
    firstNum = int(input("What's the first number?: "))
  print('+ \n - \n * \n / ')
  operation = input("Pick an operation: ")
  nextNum = int(input("What's the next number?: "))
  if operation == '+':
    exitNum = addition(firstNum, nextNum)
  elif operation == '-':
    exitNum = substraction(firstNum, nextNum)
  elif operation == '*':
    exitNum = multiplication(firstNum, nextNum)
  elif operation == '/':
    exitNum = division(firstNum, nextNum)
  ifContinue = input(f"Type 'y' to continue calculating with {exitNum}, or type 'n' to start a new calculation: ")
  if ifContinue == 'y':
    calcInput(exitNum)
  
def addition(a, b):
  return a + b

def substraction(a, b):
  return a - b

def multiplication(a, b):
  return a * b

def division(a, b):
  return a / b

calcInput()
  
