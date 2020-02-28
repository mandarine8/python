# creer une liste qui va stocker des pseudos pour simuler un jeu en ligne
# Tchoup, CherryChew, Nananas, Banana...
online_players = ["Tchoup", "Banana", "Cherrychew", "Nananas"]
print(online_players)
print(online_players[0])
print(online_players[len(online_players) -1])

# modifier Tchoup par Tchouptchoup
online_players[0] = "Tchouptchoup"
print(online_players)

online_players.insert(2, "Mandarinette")
print(online_players)

# des indices 2 à 4: [2:4]

# ajouter une valeur en bout de liste:
online_players.append("Chevrefeuille")
print(online_players)

online_players.extend(["Rhodo", "Dendron"])
print(online_players)

# supprimer u élément de la liste
del online_players[7]
print(online_players)

online_players.pop(6)
print(online_players)

#viere par le nom et pas l'indice:
online_players.remove("Chevrefeuille")
print(online_players)

# .clear pour nettoyer la liste au complet

