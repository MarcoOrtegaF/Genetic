
def knapsack_greedy(items, capacity):

  items.sort(key=lambda item: item[0] / item[1], reverse=True)

  optimal_solution = []

  for item in items:
    if item[1] <= capacity:
      optimal_solution.append(item)
      capacity -= item[1]

  return optimal_solution


# Ejemplo:

items = [(10, 2), (5, 1), (3, 1)]
capacity = 3

optimal_solution = knapsack_greedy(items, capacity)

print("\nEjemplo 1 (KP):\nItems: ",items, "\nCapacidad: ", capacity, "\nLa solucion optima es:", optimal_solution,"\n")
