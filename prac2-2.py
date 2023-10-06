
#CHANGE MAKING PROBLEM 

def change_making(coins, amount):

    n = len(coins)
    T = [[float('inf') for x in range(amount + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        T[i][0] = 0

    for i in range(n + 1):
        for j in range(amount + 1):
            if coins[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = min(T[i][j - coins[i - 1]] + 1, T[i - 1][j])

#ALGORITMO PARA ENCONTRAR LAS MONEDAS DE LA SOLUCION OPTIMA
    sol = []
    i = len(coins)
    w = amount
    while i > 0 and w > 0:
        if T[i][w] == T[i - 1][w]:
            i -= 1
        else:
            sol.append(coins[i - 1])
            w -= coins[i - 1]

    return T[n][amount], sol

# Ejemplo 1: Change making problem
coins = [25, 10, 5, 1]
amount = 23

min_coins = change_making(coins, amount)

print("\n-----> Ejemplo 1:\nDenom = \t", coins,"\nCambio =\t",amount)
print("\nMonedas de la solucion optima: ", min_coins[1])
print("Numero minimo de monedas para el cambio: ", min_coins[0])

# Ejemplo 2: Change making problem
coins = [10, 5, 2, 1]
amount = 57

min_coins = change_making(coins, amount)

print("\n-----> Ejemplo 2:\nDenom = \t", coins,"\nCambio =\t",amount)
print("\nMonedas de la solucion optima: ", min_coins[1])
print("Numero minimo de monedas para el cambio: ", min_coins[0])