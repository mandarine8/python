def addition():
  result = 5 + 5
  return result

def multiply():
  return 5 * 8


print("Le résultat de l'addition est", addition())
print("Le résultat de la multiplication est", multiply())

# with parameters
# /!\ argument qd on appelle la fonction, parametre qd on la crée
# on peut mettre une valeur par defaut en parameter si on passe pas d'argument
def param(n):
  return 5 + n

print("Le résultat de l'addition est", param(10))
