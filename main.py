import random
import time

# Prints a horizontal line.
def print_horizontal_line():
  print("________________________________________")
  print("")

# Finds all occurences of a letter in a piece of text,
# returning them all in a list of indices.
def find_letter_index_all(text, letter):
  found_letter_indices = []

  counter = 0
  for character in text:
    if character == letter:
      found_letter_indices.append(counter)
    
    counter += 1
  
  return found_letter_indices

# Prints the status of the player at a moment of the game.
def print_game_status(known_letters, lives_left, incorrect_letters):
  print((''.join(known_letters)) + " | Levens over: " + str(lives_left))
  if len(incorrect_letters) > 0:
    print("Incorrect: " + ", ".join(incorrect_letters))

# Prints the win screen.
def print_win():
  print("")
  print("Gefeliciteerd! Jij won!")

# Prints the lose screen.
def print_lose():
  print("")
  print("Gefeliciteerd! Jij verloor! Het woord was " + word + ".")

def has_number(s):
  return any(i.isdigit() for i in s)

START_LIVES = 5

# Prints instructions for the game.
print("WELKOM BIJ GALGJE!")
print_horizontal_line()
print("Dit is een spel waarbij je")
print("een woord moet raden door")
print("allerlei letters te proberen.")
print("Je hebt alleen vijf levens.")
print("Wanneer je een foute letter raadt,")
print("verlies je een leven.")

# Asks the player to press 'enter' to begin.
print("")
input("Druk op 'enter' om te beginnen...")

# Prints the loading bar before starting the game.
print("")
current_empty = "------------"
current_load = ""
for j in range(12):
  current_load += "#"
  current_empty = current_empty[1:]
  print("Loading [" + current_load + current_empty + "]", end='\r')
  time.sleep(random.uniform(0, 0.125))

print_horizontal_line()

# This is the list of words possible.
words = [
  "informatica",
  "informatiekunde",
  "spelletje",
  "aardigheidje",
  "scholier",
  "fotografie",
  "waardebepaling",
  "specialiteit",
  "verzekering",
  "universiteit",
  "heesterperk"
]

# Try again loop
while True:
  lives_left = START_LIVES

  incorrect_letters = []

  # Pick a word randomly from the list of words above.
  word = words[random.randint(0, len(words) - 1)]
  lowercased_word = word.lower();

  # Setup list of known letters with empty dashes to begin.
  known_letters = []
  for x in word:
    known_letters.append('-')

  response = ""

  # Main game loop
  while True:
    print_game_status(known_letters, lives_left, incorrect_letters)

    # Asks the player to choose a letter.
    # Makes sure to only get the first letter of the input and
    # to lowercase that letter to solidify
    # comparing processes.
    letter = input("Welk letter: ").lower()

    # Asks the player to only type in one letter.
    if len(letter) > 1:
      print("")
      print("Voer alleen maar 1 letter in.")
      print("")
      continue

    # Asks the player to only type in letters, not numbers.
    if has_number(letter):
      print("")
      print("Voer alleen maar letters in.")
      print("")
      continue

    print("")

    # Checks if the letter can be found in the word.
    # Logic comparing words and letters are all done with lowercased strings.
    # The reason for this is to keep the code safe from words containing capital letters.
    if letter in lowercased_word:
      print("GOED")
      
      same_letter_indices = find_letter_index_all(lowercased_word, letter)

      # Replaces all indices of the letter in the known letters list.
      for i in same_letter_indices:
        known_letters[i] = word[i]

      # Checks if there are any dashes left. If not, the player has won!
      if '-' not in known_letters:
        print_win()
        break
    else:
      print("FOUT")

      # Adds unique incorrect letters to the list of incorrect letters.
      if letter not in incorrect_letters:
        incorrect_letters.append(letter)
        incorrect_letters.sort()

      lives_left -= 1

      # Checks if there are no lives left. If so, the player has lost!
      if lives_left == 0:
        print_lose()
        break

    print("")

  print("")
  print("")
  print("")

  # Asks the player if he wants to play another game of Galgje.
  while response != "ja" and response != "nee":
    response = input("Wil je weer spelen? Voer in 'JA' of 'NEE': ").lower()

  # Exits the game if the player answers with N.
  if response == "nee":
    break

  print("")
  print("")
  print("")