import importlib
caesarCipherLogo = importlib.import_module("caesar-cipher-logo")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print(caesarCipherLogo.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(startText, shiftAmount, cipherDirection):
  endText = ""
  if cipherDirection == "decode":
      shiftAmount *= -1

  for letter in startText:
    if letter in alphabet:
       letterIndex = alphabet.index(letter)
       endText += alphabet[letterIndex + shiftAmount]
    else:
       endText += letter

  print(f"The {cipherDirection}d text is: {endText}")

shift = shift % 26
caesar(text, shift, direction)