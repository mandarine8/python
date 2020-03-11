# un youtubeur a une commu de 2500 abonnés
suscribers_count = 2500

# il gagne 10% d'audience supplementaire (abonnés) par mois
months = 0

# combien aura t il d'abonnés après 2 ans (24 mois)
while months <= 24:

  # augmenter l'audience
  # coefficient:
  # + 30% = 1 + 30/100 = 1.3
  # - 20% = 1 - 20/100 = 0.8
  suscribers_count *= 1.10

  # afficher le nombre d'abonnés
  print("Vous avez actuellemnt {} abonnés".format(suscribers_count))

  # on passe au mois suivant
  months += 1

