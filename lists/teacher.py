import statistics
# from statistics import mean
from random import shuffle

# systeme de notation d'eleves

# ecriture a la ligne et virgule à la fin pour se faciliter la lecture et l'ecriture

notes = [
  8, 12, 10,
  17, 9, 13,
 ]
print(notes)

# modules à importer
# mean : moyenne de toutes les notes
result = statistics.mean(notes)
# result = mean(notes)
print(result)

shuffle(notes)
print(notes)
