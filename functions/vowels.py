# fonction pour calculer le nombre de voyelles dans un mot

# definir une fonction get_vowels_numbers(mot)
# créer un compteur de voyelles
# pour chaque lettre du mot, verifier si il s'agit d'une voyelle
# si c'est le cas, ajouter 1 au compteur
# a la fin de la fonction, renvoyer le compteur

def get_vowels_number(word):
  vowel_counter = 0

  for letter in word:
    if letter in ["a","e","i","o","u","y"]:
      vowel_counter += 1
  return vowel_counter

word = input("Enter a word: ")
count = get_vowels_number(word)
print("Il y a", count, "voyelles dans le mot", word)

