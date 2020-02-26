# Système de vérification de mot de passe

password = input("Entrez votre mot de passe: ")
password_length = len(password)

# verifier si le mot de passe est inferieur à 8 caractères
if password_length <= 8:
  print("Mdp trop court")
# elif password_length > 8 and password_length < 12:
elif 8 < password_length < 12:
  print("Mdp moyen")
else:
  print("Mdp parfait!")

print(password_length)
