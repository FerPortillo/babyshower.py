def calcular_sueldo():
  vendedores = []

  while True:
      otro_vendedor = input("¿Hay otro vendedor? (si/no): ").lower()

      if otro_vendedor != 'si':
          break

      nombre = input("Ingrese el nombre del vendedor: ")
      salario_base = float(input("Ingrese el salario base de {} : ".format(nombre)))
      ventas_realizadas = float(input("Ingrese el total de ventas realizadas por {} : ".format(nombre)))

      if ventas_realizadas < 3500:
          porcentaje_comision = 0.07
      elif 3500 <= ventas_realizadas <= 7000:
          porcentaje_comision = 0.10
      else:
          porcentaje_comision = 0.15

      sueldo_total = salario_base + (ventas_realizadas * porcentaje_comision)

      vendedor = {'nombre': nombre, 'sueldo_total': sueldo_total}
      vendedores.append(vendedor)

  print("\nResultados:")
  for vendedor in vendedores:
      print("{} - Sueldo Total: ${:.2f}".format(vendedor['nombre'], vendedor['sueldo_total']))

calcular_sueldo()
