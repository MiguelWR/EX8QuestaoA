#Exercício 8

#a)

def Sa(n):
  if n == 0:
    return 1
  else:
    return 3 * Sa(n - 1)