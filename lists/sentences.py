from random import shuffle
# générateur de phrases

# demander en console une chaine de la forme mot1/mot2/mot3/mot4/...
# transformer cette chaine en une liste
# la mélanger
# si le nombre d'éléments de cette liste est inf à 10, afficher les 2 premiers mots
# si le nombre est sup ou égal à 10, afficher les 3 derniers

input_value = input("Entrez tous les mots sous la forme mot1/mot2/mot3... ")
print(input_value)

words = input_value.split("/")
print(words)

shuffle(words)
print(words)

words_length = len(words)
print(words_length)

if words_length < 10:
  print(words[0:2])
else:
  print(words[words_len - 1], words[words_len - 2], words[words_len - 3])
