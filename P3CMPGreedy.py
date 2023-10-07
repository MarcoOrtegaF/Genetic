
def change_money(Cambio, monedas):
  monedas.sort(reverse=True)

  sol_Optima = []

  for moneda in monedas:
    if moneda <= Cambio:
      sol_Optima.append(moneda)
      Cambio -= moneda

  return sol_Optima


# Ejemplo:

monedas = [1, 3, 4]
Cambio = 6

sol_Optima = change_money(Cambio, monedas)

print("\nEjemplo 1 (CMP):\n\nMonedas: ", monedas,"\nCambio: ", Cambio,"\nLa solucion optima es :", sol_Optima, "\n")
