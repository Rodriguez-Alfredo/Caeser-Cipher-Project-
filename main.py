#!/bin/python3

#define our function taking message, key, and mode 
def caesar(message, key, mode):

  #Setting up the reference
  LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  #empty sting for the output
  translated = ' '

  #Capitalize all letters
  message = message.upper()
  
  #Return the remainder of the key 
  key = key % 26
  
  #starting a for-loop
  for i in message:

    #Takes i to locate in the variable LETTERS 
    templetter = LETTERS.find(i)
    
    #add the amount of 'key' to the letter
    if mode == 'encrypt':
      templetter += key
      #print('encrypt')

    #subtract the amount of 'key' to the letter
    elif mode == 'decrypt':
      templetter -= key
      #print('Decrypt')

    #fix the issue with letters going over 26
    if templetter >= len(LETTERS):
      templetter -= len(LETTERS)

    #fix issue with letters less then 0
    elif templetter < 0:
      templetter += len(LETTERS)

    #adds value to the empty string on line 10
    translated += LETTERS[templetter]

  #return the transalted string
  return translated

print(caesar("CYBRARY", 6, "encrypt"))

print(caesar("IEHXGXE", 6, "decrypt"))

#Enter word to encrypt
print(caesar(input("Enter Word: "), 6, "encrypt"))

#Enter word to decrypt
print(caesar(input("Enter Word: "), 6, "decrypt"))