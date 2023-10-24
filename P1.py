import numpy as np

random_list = np.random.uniform(-1000, 1000, 100)

Menores = [0,0]
Mayores = [0,0]

for x in random_list:
    if(x < Menores[0]):
        Menores[1] = Menores[0]
        Menores[0] = x
    if(x > Mayores[0]):
        Mayores[1] = Mayores[0]
        Mayores[0] = x

print("\nLos Menores: " + str(Menores) + "\nLos Mayores: " + str(Mayores))