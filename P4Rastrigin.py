import numpy as np

#  FUNCION RASTRIGIN
def rastrigin(x):
    A = 10
    n = len(x)
    return A * n + sum([(xi**2 - A * np.cos(2 * np.pi * xi)) for xi in x])

# INICIALIZAR LA POBLACION
def inicPoblacion(tamPoblacion, dimension):
    poblacion = np.random.uniform(-5.12, 5.12, (tamPoblacion, dimension))
    return poblacion

# EVALUAR EL FITNESS INDIVIDUAL
def calcFitness(poblacion):
    return np.array([rastrigin(individual) for individual in poblacion])

# SELECCIONAR A LOS PADRES USANDO LA SELECCION PPOR TORNEO
def selecTorneo(poblacion, fitness, numPadres):
    seleccionado_padres = []
    for _ in range(numPadres):
        indices = np.random.choice(len(poblacion), size=2, replace=False)
        seleccionado = poblacion[indices[np.argmin(fitness[indices])]]
        seleccionado_padres.append(seleccionado)
    return np.array(seleccionado_padres)

# CROSSOVER DE TIPO "SINGLE POINT"
def crossover(padres, numHijos):
    hijos = []
    for _ in range(numHijos):
        crossover_point = np.random.randint(1, len(padres[0]))
        padre1 = padres[np.random.randint(len(padres))]
        padre2 = padres[np.random.randint(len(padres))]
        offspring = np.hstack((padre1[:crossover_point], padre2[crossover_point:]))
        hijos.append(offspring)
    return np.array(hijos)

# MUTAR CON PROBABILIDAD BAJA
def mutar(hijos, tasaMutacion):
    mutard_hijos = []
    for offspring in hijos:
        if np.random.rand() < tasaMutacion:
            mutation_point = np.random.randint(len(offspring))
            offspring[mutation_point] += np.random.uniform(-0.1, 0.1)
        mutard_hijos.append(offspring)
    return np.array(mutard_hijos)

# FUNCION PRINCIPAL
def AlgGenetico(tamPoblacion, dimension, numGeneraciones, numPadres, numHijos, tasaMutacion):
    poblacion = inicPoblacion(tamPoblacion, dimension)
    for generation in range(numGeneraciones):
        fitness = calcFitness(poblacion)
        padres = selecTorneo(poblacion, fitness, numPadres)
        hijos = crossover(padres, numHijos)
        hijos = mutar(hijos, tasaMutacion)
        poblacion[:numPadres] = padres
        poblacion[numPadres:] = hijos
        mejorFitness = min(fitness)
        print(f"Genereacion {generation}: Mejor-Fitness = {mejorFitness}")
    
    mejorSolucion = poblacion[np.argmin(fitness)]
    return mejorSolucion, rastrigin(mejorSolucion)

if __name__ == "__main__":
    tamPoblacion = 10
    dimension = 3
    numGeneraciones = 10
    numPadres = 5
    numHijos = 5
    tasaMutacion = 0.1

    mejorSolucion, mejorFitness = AlgGenetico(tamPoblacion, dimension, numGeneraciones, numPadres, numHijos, tasaMutacion)
    print(f"Mejor solucion: {mejorSolucion}")
    print(f"Mejor Fitness: {mejorFitness}")
