import random
# Imports library called colorama (to color the )
from colorama import Fore, Style 

# Gets a random word from words.txt
def get_wordle_word():
  # Open the words.txt file to read as f
  with open('words.txt', encoding='utf-8') as f:
    file = f.readlines() # Array of all lines for f
  
    wordle_index = random.randint(0, len(file) - 1) # Generate random index for wordle word
    return file[wordle_index].strip() # Get the word and return it with newline ('\n') removed

# Checks if a guess is valid
# PARAMETER: guess - The inputted guess from user
def valid_guess(guess):
  # Open the words.txt file to read as f
  with open('words.txt', encoding='utf-8') as f:
    file = f.readlines() # Array of all lines of f
 
    # Repeat for each element in file array (the element in use is named word)
    for word in file:
      # Checks if guess is inside the array
      if guess == word.strip():
        return True # If so, return True
  return False # If word is not in file, return false

# Asks user for guess until its a valid word, and then returns the word
def get_guess():
  guess = "" # Variable which holds user guess

  # Loops until user guess is valid
  while not valid_guess(guess):
    guess = input("Enter a guess: ") # Asks user for guess
  return guess # Returns guess value once guess is valid

# Color the user's guess
# PARAMETER: guess - The inputted guess to be checked (from the user)
# PARAMETER: wordle_word - The word which the guess is being checked against
def color_guess(guess, wordle_word):
  colored_guess = [] # Array which will hold the colored version of the guess

  # Loops through indices from 0 to the length of the guess string (exclusive)
  for i in range(len(guess)):
    # If the guess's letter for that index is the same as the wordle_word's letter for that inde
    if guess[i] == wordle_word[i]:
      # Put into the array of colored letters the guess letter colored in green
      colored_guess.append(f'{Fore.GREEN}{guess[i]}{Style.RESET_ALL}')
    # Else if the guess letter is anywhere in the wordle_word
    elif guess[i] in wordle_word:
      # Put into the array of colored letters the guess letter colored in yellow
      colored_guess.append(f'{Fore.YELLOW}{guess[i]}{Style.RESET_ALL}')
    # Else (the guess's letter is not in the wordle_word)
    else:
      # Just put the letter (no coloring) into the array of letters
      colored_guess.append(guess[i])

  return colored_guess # Returns the colored array

# Test if color works
print(' '.join(color_guess(get_guess(), 'crane')))


