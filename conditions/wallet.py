# on enleve les dernieres lignes avec l'appel de la fonction main

wallet = 15000
computer_price = 900
car_price = 10000

# est ce que le prix de l'ordinateur est inferieur à 1000€
print(computer_price < 1200)

if computer_price < 1000:
  print("Le prix de l'ordinateur est inferieur à 1000€")
else:
  print("Le prix est supérieur")

if car_price <= wallet:
  print("L'achat de la voiture est possible")
  # wallet = wallet - car_price
  wallet -= car_price
  print("Il vous reste {}€ dans votre porte monnaie".format(wallet))
else:
  print("Vous n'avez pas assez d'argent pour cet achat")

# and et or pour verifier 2 conditions a la fois
# on peut aussi simplifier:
# if computer_price < 1000 and computer_price > 500
# if 1000 < computer_price > 500

# conditions ternaires
text = ("L'achat est impossible", "L'achat est possible")[computer_price <= 1000]
print(text)
print(wallet)
