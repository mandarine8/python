# jeu du juste prix

# choisir un nombre entre 1 et 1000
# le joueur annonce la valeur
# tant que le jeu n'est pas fini,
  # demander à l'utilisateur d'entrer un prix
  # si il trouve le juste prix "c'est gagné"
  # sinon "c'est moins" ou "c'est plus"

# importation du randint
from random import randint

winning_number = randint(1,1000)

# statut du jeu (activé/désactivé)
running = True

# tant que le jeu est en cours d'éxécution
while running:

    # demander à l'utilisateur d'entrer un prix dans la console
    picked_number = int(input("Choose a number "))

    # si le prix est le meme que le juste prix
    if picked_number == winning_number:
      print("Good job !")
    # fin du jeu
      running = False

    # si le prix de l'utilisateur est supérieur au prix à trouver
    elif picked_number > winning_number:
      print("C'est moins")

    # si le prix de l'utilisateur est inférieur au prix à trouver
    elif picked_number < winning_number:
      print("C'est plus")

# fin du jeu après la boucle
print("End of the game !")

