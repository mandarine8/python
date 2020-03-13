def add(a):
  a += 1
  print(a)
  # recursivité pour boucler la fonction:
  if a < 50:
    add(a)

add(5)
