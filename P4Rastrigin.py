import numpy as np

# FUNCION RASTRIGIN
def rastrigin(x):
    A = 10
    return A * 3 + np.sum(x**2 - A * np.cos(2 * np.pi * x))

# PARAMETROS DEL ALGORITMO GENETICO
tamPoblacion = 150
tamGeneraciones = 150
tasaMutacion = 0.1
tasaCrossover = 0.8

# INICIALIZACION
dim = 3
cotaInferior = -5.12
cotaSuperior = 5.12
poblacion = np.random.uniform(cotaInferior, cotaSuperior, (tamPoblacion, dim))

for generacion in range(tamGeneraciones):
    # CALCULAR EL FITNEES PARA CADA INDIVIDUO
    fitness = np.array([rastrigin(x) for x in poblacion])

    # SELECCIONAR EL INDIVIDUO BASADO EN EL FITNESS PARA REPRODUCCION 
    indexSeleccionados = np.argsort(fitness)

    # CREAR UNA NUEVA POBLACION ATRAVES DEL CROSSOVER Y MUTACION
    nuevvaPoblacion = np.empty_like(poblacion)
    for i in range(0, tamPoblacion, 2):
        padre1 = poblacion[indexSeleccionados[i]]
        padre2 = poblacion[indexSeleccionados[i + 1]]

        # CROSSOVER
        if np.random.rand() < tasaCrossover:
            puntoCrossover = np.random.randint(dim)
            hijo1 = np.concatenate((padre1[:puntoCrossover], padre2[puntoCrossover:]))
            hijo2 = np.concatenate((padre2[:puntoCrossover], padre1[puntoCrossover:]))
        else:
            hijo1 = padre1
            hijo2 = padre2

        # MUTACION
        if np.random.rand() < tasaMutacion:
            puntoMutacion = np.random.randint(dim)
            hijo1[puntoMutacion] = np.random.uniform(cotaInferior, cotaSuperior)
        if np.random.rand() < tasaMutacion:
            puntoMutacion = np.random.randint(dim)
            hijo2[puntoMutacion] = np.random.uniform(cotaInferior, cotaSuperior)

        nuevvaPoblacion[i] = hijo1
        nuevvaPoblacion[i + 1] = hijo2

    poblacion = nuevvaPoblacion

# ENCONTRAR LA MEJOR SOLUCION EN LA POBLACION FINAL
fitnessFinal = np.array([rastrigin(x) for x in poblacion])
mejorSolucion = poblacion[np.argmin(fitnessFinal)]
menorFitness = min(fitnessFinal)

print("\n\nMejor solucion:", mejorSolucion)
print("Fitness Minimo:", menorFitness)
