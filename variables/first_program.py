def main():
  # recolter une premiere note
  note1 = int(input("Entrez la première note: "))
  # recolter une deuxieme note
  note2 = int(input("Entrez la deuxième note: "))
  # recolter une derniere note
  note3 = int(input("Entrez la troisième note: "))
  # Calcul de la moyenne
  result = (note1 + note2 + note3) / 3
  # Afficher le resultat
  print("La moyenne de l'élève est " + str(result))

if __name__ == '__main__':
  main()
