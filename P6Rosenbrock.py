import numpy as np
import random

# FUNCION ROSENBROCK
def rosenbrock(x, y, z):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2 + (1 - z) ** 2 + 100 * (y - z ** 2) ** 2

# PARAMETROS PSO
NumPaticulas = 50
NumDim = 3
maxIteraciones = 150
c1 = 1.496
c2 = 1.496
w = 0.729

# INICIALIZAR PARTICULAS
particulas = np.random.rand(NumPaticulas, NumDim)
velParticulas = np.random.rand(NumPaticulas, NumDim)
mejoresPosisParticula = particulas.copy()
mejorPosGlobal = particulas[random.randint(0, NumPaticulas - 1)].copy()
mejorValGlobal = rosenbrock(*mejorPosGlobal)

for iteraciones in range(maxIteraciones):
    for i in range(NumPaticulas):
        particula = particulas[i]
        velocidad = velParticulas[i]
        mejorPosParticula = mejoresPosisParticula[i]

        # ACTUALIZAR VELOCIDAD DE LA PARTICULA
        r1, r2 = random.random(), random.random()
        velocidad = (w * velocidad +
                    c1 * r1 * (mejorPosParticula - particula) +
                    c2 * r2 * (mejorPosGlobal - particula))
        velParticulas[i] = velocidad

        # ACTUALIZAR POSICION DE LA PARTICULA
        particula += velocidad
        particulas[i] = particula

        # ACTUALIZAR LA MEJOR POSICION Y LA POSICION GLOBAR DE LA PARTICULA
        valorActual = rosenbrock(*particula)
        if valorActual < rosenbrock(*mejorPosParticula):
            mejoresPosisParticula[i] = particula.copy()
        if valorActual < mejorValGlobal:
            mejorPosGlobal = particula.copy()
            mejorValGlobal = valorActual

    print(f"iteracion {iteraciones}: Mejor Valor Global = {mejorValGlobal}")

print("\n\nSolucion Optima:")
print("x =", mejorPosGlobal[0])
print("y =", mejorPosGlobal[1])
print("z =", mejorPosGlobal[2])
print("Valor Minimo =", mejorValGlobal)
