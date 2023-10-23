import numpy as np
import random

# DEFINICION DE LA FUNCION ACKLEY
def ackley(x, y):
    a = 20
    b = 0.2
    c = 2 * np.pi
    return -a * np.exp(-b * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(c * x) + np.cos(c * y))) + a + np.exp(1)

# PARAMETROS DEL ALGORITMO GENETICO
tamPobla = 10
numGene = 10
tasaMuta = 0.1

# DEFINIR LA POBLACION INICIAL
def inicPoblacion(size):
    return [(random.uniform(-5, 5), random.uniform(-5, 5)) for _ in range(size)]

# CALCULA EL FITNESS DE CADA INDIVIDUO
def calcFitness(individual):
    x, y = individual
    return ackley(x, y)

# SELECCIONA LOS PADRES PARA REPRODUCCION USANDO EL METODO DE COMPETEMCIA
def selecTorneo(poblacion, k=5):
    tournament = random.sample(poblacion, k)
    return min(tournament, key=calcFitness)

# CROSSOVER DE TIPO "SINGLE POINT"
def crossover(padre1, padre2):
    x1, y1 = padre1
    x2, y2 = padre2
    crossover_point = random.randint(0, 1)
    if crossover_point == 0:
        return (x1, y2)
    else:
        return (x2, y1)

# MUTACION IDIVIDUAL
def mutar(individual, tasaMuta):
    x, y = individual
    if random.random() < tasaMuta:
        return (x + random.uniform(-0.1, 0.1), y + random.uniform(-0.1, 0.1))
    else:
        return individual

# LOOP PARA EJECUTAR TODO EL ALGORITMO GENETICO
poblacion = inicPoblacion(tamPobla)

for generation in range(numGene):
    poblacion = sorted(poblacion, key=calcFitness)
    new_poblacion = []

    # ELITISMO: MANTIENE AL MEJOR INDIVIDUAL
    new_poblacion.append(poblacion[0])

    # CREAR A LA SIGUIENTE GENERACION
    while len(new_poblacion) < tamPobla:
        padre1 = selecTorneo(poblacion)
        padre2 = selecTorneo(poblacion)
        hijo = crossover(padre1, padre2)
        hijo = mutar(hijo, tasaMuta)
        new_poblacion.append(hijo)

    poblacion = new_poblacion

mejorSolu = poblacion[0]
mejorFitness = calcFitness(mejorSolu)

print(f"Mejor solucion: {mejorSolu}")
print(f"Mejor fitness: {mejorFitness}\n")
