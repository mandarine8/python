# creer une fonction max qui va renvoyer le resultat le plus haut entre 2 valeurs

def max(a, b):
  if a > b:
    return a
  else:
    return b

first_value = int(input("Entrez la valeur de a: "))
second_value = int(input("Entrez la valeur de b: "))

max_value = max(first_value, second_value)

print("La valeur max est", max_value)
