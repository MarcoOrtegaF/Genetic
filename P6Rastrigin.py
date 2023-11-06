import numpy as np
import random

# DEFINICION DE LA FUNCION RASTRIGIN 
def rastrigin(x):
    A = 10
    return A * len(x) + sum([(xi**2 - A * np.cos(2 * np.pi * xi)) for xi in x])

# PARAMETROS DEL ALGORITMO PSO
numParticulas = 50
numDimensiones = 4
MaxIteraciones = 40
c1 = 1.496
c2 = 1.496
w = 0.729

# INICIALIZAR PARTICULAS
particulas = np.random.rand(numParticulas, numDimensiones)
velParticula = np.random.rand(numParticulas, numDimensiones)
mejoresPosisParticula = particulas.copy()
mejorPosGlobal = particulas[random.randint(0, numParticulas - 1)].copy() 
mejorValGlobal = rastrigin(mejorPosGlobal)

for iteraciones in range(MaxIteraciones):
    for i in range(numParticulas):
        particula = particulas[i]
        velocidad = velParticula[i]
        mejorPosParticula = mejoresPosisParticula[i]

        # ACTUALIZAR LA VELOCIDAD DE LA PARTICULA 
        r1, r2 = random.random(), random.random()
        velocidad = (w * velocidad +
                    c1 * r1 * (mejorPosParticula - particula) +
                    c2 * r2 * (mejorPosGlobal - particula))
        velParticula[i] = velocidad

        # ACTUALIZAR LA POSICION DE LA PARTICULA 
        particula += velocidad
        particulas[i] = particula

        # ACTUALIZAR LA MEJOR POSICION DE LA PARTICULA Y L AMEJOR POSICION GLOBAL
        valorActual = rastrigin(particula)
        if valorActual < rastrigin(mejorPosParticula):
            mejoresPosisParticula[i] = particula.copy()
        if valorActual < mejorValGlobal:
            mejorPosGlobal = particula.copy()
            mejorValGlobal = valorActual

    print(f"Iteraciones {iteraciones}: Major Valor Global = {mejorValGlobal}")

print("\n\nSolucion Optima:")
print("x =", mejorPosGlobal)
print("Valor Minimo =", mejorValGlobal)
