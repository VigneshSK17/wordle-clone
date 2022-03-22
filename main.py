import random

# Get all random words from words.txt
def get_random_word():
  # Create words array
  words = []
  # Open the words file
  with open("words.txt", encoding="utf-8") as f:
    # Get array with every word from words.txt
    words = f.readlines()
    # Generate random number for wordle word
    rand = random.randint(0, len(words) - 1)
    # Get the word with generated index
    return words[rand]
    
    # Oneliner version
    # return words[random.randint(0,len(words) - 1)].strip()

print(get_random_word())