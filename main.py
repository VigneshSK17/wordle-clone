import random

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

get_guess()


