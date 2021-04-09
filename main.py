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

def print_game_statue(known_letters, lives_left):
  print((''.join(known_letters)) + " | Levens over: " + str(lives_left))

def print_win():
  print("")

  for i in range(100):
    print("Gefeliciteerd! Jij won!")
    time.sleep(0.1)

  exit()

def print_lose():
  print("")

  for i in range(100):
    print("Gefeliciteerd! Jij verloor! Het woord was " + word + ".")
    time.sleep(0.1)
  
  exit()

START_LIVES = 5

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

print("")
currentEmpty = "------------"
currentLoad = ""
for j in range(12):
  currentLoad += "#"
  currentEmpty = currentEmpty[1:]
  print("Loading [" + currentLoad + currentEmpty + "]", end='\r')
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
lowercasedWord = word.lower();

knownLetters = []
for x in word:
  knownLetters.append('-')

while True:
  print_game_statue(knownLetters, lives_left)

  letter = input("Welk letter: ")[0].lower()

  if letter in lowercasedWord:
    same_letter_indices = find_letter_index_all(lowercasedWord, letter)

    for i in same_letter_indices:
      knownLetters[i] = word[i]

    if '-' not in knownLetters:
      print_win()
  else:
    lives_left -= 1

    if lives_left == 0:
      print_lose()

  print("")