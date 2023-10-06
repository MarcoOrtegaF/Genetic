
#KNAPSACK PROBLEM

def knapsack(W, wt, val, n):

    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

#ALGORITMO PARA ENCONTRAR LAS MONEDAS DE LA SOLUCION OPTIMA

    sol = []
    i = n
    w = W
    while i > 0 and w > 0:
        if K[i][w] > K[i - 1][w]:
            sol.append(i - 1)
            w -= wt[i - 1]
        i -= 1

    return K[n][W], sol


# Ejemplo 1: Knapsack problem
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

max_val = knapsack(W, wt, val, n)

print("\n-----> Ejemplo 1:\nVal: \t", val,"\nwt =\t",wt, "\nW = ", W)
print("Objetos de la solucion optima: ", max_val[1])
print("Valor maximo en la mochila: ", max_val[0])

# Ejemplo 2: Knapsack problem
val = [5, 2, 6, 4, 1, 3]
wt = [10, 15, 13, 20, 25, 5]
W = 50
n = len(val)

max_val = knapsack(W, wt, val, n)

print("\n-----> Ejemplo 2:\nVal: \t", val,"\nwt =\t",wt, "\nW = ", W)
print("Objetos de la solucion optima: ", max_val[1])
print("Valor maximo en la mochila: ", max_val[0])