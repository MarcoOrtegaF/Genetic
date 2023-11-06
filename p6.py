import numpy as np
import random

# Define Rosenbrock's function
def rosenbrock(x, y, z):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2 + (1 - z) ** 2 + 100 * (y - z ** 2) ** 2

# PSO parameters
numParticulas = 50
numDim = 3
Iteraciones = 400
c1 = 1.496
c2 = 1.496
w = 0.729

# Initialize particulas
particulas = np.random.rand(numParticulas, numDim)
velParticulas = np.random.rand(numParticulas, numDim)
mejorPosParticula = particulas.copy()
mejorPosGlobal = particulas[random.randint(0, numParticulas - 1)].copy()
mejorValGlobal = rosenbrock(*mejorPosGlobal)

for iteracion in range(Iteraciones):
    for i in range(numParticulas):
        particula = particulas[i]
        velocidad = velParticulas[i]
        mejorPosParticula = mejorPosParticula[i]

        # Update particula velocidad
        r1, r2 = random.random(), random.random()
        velocidad = (w * velocidad +
                    c1 * r1 * (mejorPosParticula - particula) +
                    c2 * r2 * (mejorPosGlobal - particula))
        velParticulas[i] = velocidad

        # Update particula position
        particula += velocidad
        particulas[i] = particula

        # Update particula best position and global best position
        current_value = rosenbrock(*particula)
        if current_value < rosenbrock(*mejorPosParticula):
            mejorPosParticula[i] = particula.copy()
        if current_value < mejorValGlobal:
            mejorPosGlobal = particula.copy()
            mejorValGlobal = current_value

    print(f"iteracion {iteracion}: Mejor Valor Global = {mejorValGlobal}")

print("\n\nSolucion Optima:")
print("x =", mejorPosGlobal[0])
print("y =", mejorPosGlobal[1])
print("z =", mejorPosGlobal[2])
print("Valor Minimo =", mejorValGlobal)
