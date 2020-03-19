text = input("Entrez une chaine de la forme (email-pseudo-mdp) ").split("-")
print(text)

print("Salut {}, ton email est {} et ton mdp {}".format(text[1], text[0], text[2]))
