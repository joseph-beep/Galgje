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
currentLoadingText = "Loading"
for i in range(3):
  for j in range(5):
    currentLoadingText += "."
    print(currentLoadingText, end='\r')
    time.sleep(0.25)

  currentLoadingText = "Loading"
  print(currentLoadingText)

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

word = words[random.randint(0, len(words) - 1)]
lowercasedWord = word.lower();

knownLetters = []
for x in word:
  knownLetters.append('-')

while True:
  print(''.join(knownLetters))

  letter = input("Welk letter: ")[0].lower()

  if letter in lowercasedWord:
    same_letter_indices = find_letter_index_all(lowercasedWord, letter)

    for i in same_letter_indices:
      knownLetters[i] = word[i]