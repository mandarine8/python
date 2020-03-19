def next_year():
  # pour rappatrier la variable dans la fonction
  global year
  print("Fin de l'année ", year)
  year += 1
  print("Début de l'année", year)

year = 2020
next_year()
