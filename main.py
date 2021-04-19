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

incorrect_letters = []

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

lives_left = START_LIVES

# Pick a word randomly from the list of words above.
word = words[random.randint(0, len(words) - 1)]
lowercased_word = word.lower();

# Setup list of known letters with empty dashes to begin.
known_letters = []
for x in word:
  known_letters.append('-')

# Try again loop
while True:
  response = ""

  # Main game loop
  while True:
    print_game_status(known_letters, lives_left, incorrect_letters)

    # Asks the player to choose a letter.
    # Makes sure to only get the first letter of the input and
    # to lowercase that letter to solidify
    # comparing processes.
    letter = input("Welk letter: ").lower()

    if len(letter) > 1:
      print("")
      print("Voer alleen maar 1 letter in.")
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

      if letter not in incorrect_letters:
        incorrect_letters.append(letter)

      lives_left -= 1

      # Checks if there are no lives left. If so, the player has lost!
      if lives_left == 0:
        print_lose()
        break

    print("")

  print("")
  print("")
  print("")

  while response != "Y" and response != "N":
    response = input("Wil je weer spelen? Y = Ja; N = Nee. Voer in: ")

  if response == "N":
    break