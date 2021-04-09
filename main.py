import random
import time

def print_horizontal_line():
  print("________________________________________")
  print("")

def find_letter_index_all(text, letter):
  found_letter_indices = []

  counter = 0
  for character in text:
    if character == letter:
      found_letter_indices.append(counter)
    
    counter += 1
  
  return found_letter_indices

def print_game_status(known_letters, lives_left):
  print((''.join(known_letters)) + " | Levens over: " + str(lives_left))

def print_win():
  print("")

  for i in range(100):
    print("Gefeliciteerd! Jij won!")
    time.sleep(0.1)

def print_lose():
  print("")

  for i in range(100):
    print("Gefeliciteerd! Jij verloor! Het woord was " + word + ".")
    time.sleep(0.1)

START_LIVES = 5

# Prints instructions for the game.
print("WELKOM BIJ GALGJE!")
print_horizontal_line()
print("Dit is een spel waarbij je")
print("een woord moet raden door")
print("allerlei letters te proberen.")
print("Je hebt alleen vijf levens.")
print("Wanneer je een foute letter raadt,")
print("Verlies je een leven.")

print("")
input("Druk op enter om te beginnen...")

# Prints the loading bar before starting the game.
print("")
current_empty = "------------"
current_load = ""
for j in range(12):
  current_load += "#"
  current_empty = current_empty[1:]
  print("Loading [" + current_load + current_empty + "]", end='\r')
  time.sleep(random.uniform(0, 0.5))

print_horizontal_line()

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

word = words[random.randint(0, len(words) - 1)]
lowercased_word = word.lower();

known_letters = []
for x in word:
  known_letters.append('-')

# Main game loop
while True:
  print_game_status(known_letters, lives_left)

  letter = input("Welk letter: ")[0].lower()

  print("")

  # Checks if the letter can be found in the word.
  # Logic comparing words and letters are all done with lowercased strings.
  # The reason for this is to keep the code safe from words containing capital letters.
  if letter in lowercased_word:
    print("GOED")

    same_letter_indices = find_letter_index_all(lowercased_word, letter)

    for i in same_letter_indices:
      known_letters[i] = word[i]

    if '-' not in known_letters:
      print_win()
      break
  else:
    print("FOUT")

    lives_left -= 1

    if lives_left == 0:
      print_lose()
      break

  print("")