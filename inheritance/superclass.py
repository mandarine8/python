class Player:

  def __init__(self, pseudo, health, attack):
    self.pseudo = pseudo
    self.health = health
    self.attack = attack

    print("Bienvenue au joueur", pseudo, " / Points de vie: ", health, " / Attaque: ", attack)

  def get_pseudo(self):
    return self.pseudo

  def get_health(self):
    return self.health

  def get_attack_value(self):
    return self.attack

  def damage(self, damage):
    self.health -= damage

  def attack_player(self, target_player):
    target_player.damage(self.attack)



class Warrior(Player):

  def __init__(self, pseudo, health, attack):
    super().__init__(pseudo, health, attack)
    self.armor = 3

    print("Bienvenue au guerrier", pseudo, " / Points de vie: ", health, " / Attaque: ", attack)

  def damage(self, damage):
    if self.armor > 0:
      self.armor -= 1
      damage = 0
    super().damage(damage)

  def blade(self):
    self.armor = 3
    print("Les points d'armure ont été rechargés")

  def get_armor_point(self):
    return self.armor



player1 = Player("Tchoup", 20, 3)
player1.damage(3)

warrior = Warrior("Banana", 30, 4)
warrior.damage(4)
print("Vie: ", warrior.get_health(), "Armure: ", warrior.get_armor_point())

warrior.damage(4)
print("Vie: ", warrior.get_health(), "Armure: ", warrior.get_armor_point())

warrior.damage(4)
print("Vie: ", warrior.get_health(), "Armure: ", warrior.get_armor_point())

warrior.damage(4)
print("Vie: ", warrior.get_health(), "Armure: ", warrior.get_armor_point())


if issubclass(Warrior, Player):
  print("Le guerrier est bien une spécialisation de player")
