def main():
  # recolter une valeur porte monnaie
  wallet = int(input("Entrer le nombre d'€ que vous possedez: "))
  print("Vous avez actuellement " + str(wallet) + "euros")

  # creer un produit qui aura pour valeur 50
  product = 50
  print("Le Produit vaut " + str(product) + "euros")

  # enleve au "wallet" le prix du produit
  wallet = wallet - product
  # ou wallet -= produit

  # afficher la nouvelle valeur
  print("Produit acheté !")
  print("Il ne vous reste plus que", wallet, "euros")


if __name__ == '__main__':
  main()
