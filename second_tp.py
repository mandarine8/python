# Place de cinema
# Recolter l'age de la personne qui achete les billets ("Quel est ton age?")

age = int(input("Quel est ton age? "))

# si la personne est mineure elle devra payer 7€
if age < 18:
  print("Ton billet est à 7€")
  price = 7
# si la personne est majeure, elle paiera 12€
else:
  print("Tu dois payer 12€")
  price = 12

# souhaitez-vous du popcorn ?
popcorn = input("Veux-tu du popcorn? ")

# si oui +5€
if popcorn == "oui":
  print("C'est 5€ supplementaire")
  price += 5
else:
  print("c'est noté")

# afficher le prix total à payer
print("Votre total est de " + str(price) + "€")
