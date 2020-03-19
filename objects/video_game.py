from weapon import Weapon
# class pour faire le moule, l'objet
class Player:
  # a l'interieur on met les attributs, les caracteristiques, pour les fixer
  # pseudo = "Tchoup"
  # health = 20
  # attack = 3

  # definir une fonction qui va etre la premiere à s'intitialiser qd on va
  # creer une instance de l'objet player = constructeur
  # self = 1er parametre qui se genere automatiquement = contexte par defaut
  def __init__(self, pseudo, health, attack):
    # creer un nouvel attribut et affecter la valeur
    self.pseudo = pseudo
    self.health = health
    self.attack = attack
    self.weapon = None

    print("Bienvenue au joueur", pseudo, " / Points de vie: ", health, " / Attaque: ", attack)

  # methode = fonction mais dans le cadre d'une classe
  # getter / assessor = pour recuperer les infos
  def get_pseudo(self):
    return self.pseudo

  def get_health(self):
    return self.health

  def get_attack_value(self):
    return self.attack

  # setter / mutator = modifier des valeurs
  def damage(self, damage):
    self.health -= damage
    print("Aie, vous venez de subir", damage, "dégats!")

  # autres méthodes
  def attack_player(self, target_player):
    target_player.damage(self.attack)

    # si le joueur a une arme
    #if self.has_weapon():
        # ajoute les dégats de l'arme au point d'attaque du joueur
        #damage += self.weapon.get_damage_amount()

    #target_player.damage(damage)

  # méthode pour changer l'arme du joueur
  #def set_weapon(self, weapon):
      #self.weapon = weapon

  # méthode pour verifier si le joueur a une arme
  #def has_weapon(self):
      #return self.weapon is not None


#knife = Weapon("Couteau", 3)



# on sort de ce moule et on crée une nouvelle instance de l'objet player
# notion de constructeur: spécifier les valeurs, les paramètres entre ()
player1 = Player("Tchoup", 20, 3)
player2 = Player("Mat", 19, 2)
# print("Bienvenue au joueur", player1.pseudo)

print("Pseudo:", player1.get_pseudo())

player1.damage(3)
print("Vous possédez maintenant", player1.get_health(), "points de vie")

player1.attack_player(player2)
print(player1.get_pseudo(), "attaque", player2.get_pseudo())
print("Bienvenue au joueur", player1.get_pseudo(), " / Points de vie: ", player1.get_health(), " / Attaque: ", player1.get_attack_value())
print("Bienvenue au joueur", player2.get_pseudo(), " / Points de vie: ", player2.get_health(), " / Attaque: ", player2.get_attack_value())
