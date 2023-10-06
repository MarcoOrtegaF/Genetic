import numpy as np

# Define a list with 100 random floating point numbers between -1000 and 1000
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

# Print the list
print("Los Menores: " + str(Menores) + "\nLos Mayores: " + str(Mayores))