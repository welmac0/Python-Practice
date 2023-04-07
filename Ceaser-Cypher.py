alphabet = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def decode():
  message = input('Type your message: ').lower()
  shift = int(input('Type the shift number: '))
  encoded = ''
  for letter in message:
    try:
      index = alphabet.index(letter)
      newIndex = index - shift
      if newIndex < 0:
        newIndex = newIndex + len(alphabet)
      finalLetter = alphabet[newIndex]
    except:
      finalLetter = letter
    encoded = encoded + finalLetter
  print(f"Here's decoded result: {encoded}")
  whetherContinue()


def encode():
  message = input('Type your message: ').lower()
  shift = int(input('Type the shift number: '))
  encoded = ''
  for letter in message:
    try:
      index = alphabet.index(letter)
      newIndex = index + shift
      if newIndex > len(alphabet):
        newIndex = newIndex - len(alphabet)
      finalLetter = alphabet[newIndex]
    except:
      finalLetter = letter
    encoded = encoded + finalLetter
  print(f"Here's encoded result: {encoded}")
  whetherContinue()


def init():
  print("Type 'encode' to encrypt, type 'decode' to decrypt:")
  type = input().lower()
  if type == 'encode':
    encode()
  elif type == 'decode':
    decode()


def whetherContinue():
  print("Type 'yes' if you want to go again. Otherwise type 'no'.")
  typo = input().lower()
  if typo == 'yes':
    init()


init()
