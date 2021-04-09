import random

def print_horizontal_line():
  print("--------------------------")

print("WELKOM BIJ GALGJE!")
print_horizontal_line()
print("Dit is een spel waarbij je")
print("een woord moet raden door")
print("allerlei letters te proberen.")
print("Je hebt alleen vijf levens.")
print("Wanneer je een foute letter raadt,")
print("Verlies je een leven.")

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
  letter = input("Welk letter: ")[0].lower()

  if letter in lowercasedWord:
    knownLetters[lowercasedWord.index(letter)] = word[lowercasedWord.index(letter)]