# simulateur de ville

# créer 3 classes: immeuble, supermarché et banque
# superclass Batiment, la classe mère
# creer 4 immeubles, 2 supermarchés et 1 banque avec les valeurs de mon choix

class Building:

  def __init__(self, address, nb_floor):
    self.address = address
    self.nb_floor = nb_floor

  def get_address(self):
    return self.address

  def get_nb_floor(self):
    return self.nb_floor


class Habitation(Building):

  def __init__(self, address, nb_floor, nb_balcony):
    super().__init__(address, nb_floor)
    self.nb_balcony = nb_balcony

  def get_nb_balcony(self):
    return self.nb_balcony


class Supermarket(Building):

  def __init__(self, address, nb_floor, nb_shelves):
    super().__init__(address, nb_floor)
    self.nb_shelves = nb_shelves

  def get_nb_shelves(self):
    return self.nb_shelves


class Bank(Building):

  def __init__(self, address, nb_floor, nb_safes, name):
    super().__init__(address, nb_floor)
    self.nb_safes = nb_safes
    self.name = name

  def get_nb_safes(self):
    return self.nb_safes

  def get_name(self):
    return self.name


habitation1 = Habitation("Montreal", 3, 3)
habitation2 = Habitation("Quebec", 5, 5)
habitation3 = Habitation("Marseille", 1, 5)
habitation4 = Habitation("Praz", 3, 30)

supermarket1 = Supermarket("Montreal", 3, 100)
supermarket2 = Supermarket("NYC", 5, 5000)

bank1 = Bank("Montreal", 10, 1000, "Desjardins")

