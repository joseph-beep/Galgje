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