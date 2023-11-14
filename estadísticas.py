contar = 0
categoria1 = 0
categoria2 = 0 
categoria3 = 0
categoria4 = 0
animal = input("Quieres empezar a contar animales? (si/no)")
while animal.lower() == "si":
  contar += 1
  print(contar)
  edad = int(input("Qué edad tiene el animal?"))
  animal = input("Quieres contar más animales? (si/no)")
  if edad < 2:
    categoria1 += 1
  elif edad >= 2 and edad < 5:
    categoria2 += 1
  elif edad >= 5 and edad < 10:
    categoria3 += 1
  elif edad >= 10:
    categoria4 += 1
  porcentaje1 = categoria1*100/contar
  porcentaje2 = categoria2*100/contar
  porcentaje3 = categoria3*100/contar
  porcentaje4 = categoria4*100/contar
  print(f"Total de animales:", {contar})
  print(f"Categoria 1:", {porcentaje1})
  print(f"Categoria 2:", {porcentaje2})
  print(f"Categoria 3:", {porcentaje3})
  print(f"Categoria 4:", {porcentaje4})
