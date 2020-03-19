print("Vous êtes le client n°1")
print("Vous êtes le client n°2")
print("Vous êtes le client n°3")
print("Vous êtes le client n°4")
print("Vous êtes le client n°5")

# FOR : pour une valeur de départ (1) jusqu'à une valeur d'arrivée (5)

print("And with a loop ...")

# la derniere valeur du range est exclue alors on rajoute 1
for num_customer in range(1,6):
  print("Vos êtes le client n°", num_customer)

# FOR EACH : pour chaque valeur d'une liste donnée

print("Email envoyé à: tchoup@gmail.com")
print("Email envoyé à: banana@gmail.com")
print("Email envoyé à: mat@gmail.com")

# lister les emails
emails = ["tchoup@gmail.com", "banana@gmail.com", "mat@gmail.com"]

print("And with another loop...")

blacklist = ["mat@gmail.com"]

# pour chacune des valeurs, j'affiche "Email envoyé à:" [INSERER EMAIL]
for email in emails:
  if email in blacklist:
    print("Email {} forbidden, sending impossible".format(email))
    # pour passer au tour de boucle suivant sans afficher la suite
    continue
    # ou 'break' pour carrement casser la boucle
  print("Email envoyé à:", email)


# WHILE : tant qu'une condition est vraie

# un salarié recoit 1500$ / mois
print("Votre salaire est de 1500$")
salary = 1500

# tant que salaire < 2000 $, + 120$
while salary < 2000:
  # ajouter 120$ au salaire
  salary += 120
  # afficher le resultat
  print("Votre salaire actuel est de: ", salary, "$")
print("Vous n'avez plus droit à l'augmentation, votre salaire dépasse 2000$")
