import random

#DEFINIMOS LOS PARAMETROS DEL PROBLEMA Y LOS DEL ALGORITMO
items = [
    {"weight": 2, "value": 1},
    {"weight": 2, "value": 2},
    {"weight": 3, "value": 4},
    {"weight": 4, "value": 5},
    {"weight": 6, "value": 5},
    {"weight": 7, "value": 6},
    {"weight": 9, "value": 7},
]

W = 10
tamPoblacion = 50
generaciones = 100
tasaMutacion = 0.5

# INICIALIZAR LA POBLACION
def InicPoblacion():
    return [random.choice([0, 1]) for _ in range(len(items))]

def fitness(individual):
    pesoTotal = sum(item["weight"] for i, item in enumerate(items) if individual[i])
    if pesoTotal > W:
        return 0  # PENALIZA SI EXCEDE EL TAMANIO DEL KANPSACK
    valorTotal = sum(item["value"] for i, item in enumerate(items) if individual[i])
    return valorTotal

def crossover(padre1, padre2):
    puntoCross = random.randint(1, len(padre1) - 1)
    hijo = padre1[:puntoCross] + padre2[puntoCross:]
    return hijo

def mutar(individual):
    for i in range(len(individual)):
        if random.random() < tasaMutacion:
            individual[i] = 1 - individual[i]  # CAMBIA EL BIT

# CICLO PRINCIPAL DEL GA
poblacion = [InicPoblacion() for _ in range(tamPoblacion)]

for generation in range(generaciones):
    poblacion = sorted(poblacion, key=lambda x: -fitness(x))
    nuevaPoblacion = []

    for _ in range(tamPoblacion // 2):
        padre1, padre2 = random.choices(poblacion[:10], k=2)  # Select the top 10 individuals
        hijo1 = crossover(padre1, padre2)
        hijo2 = crossover(padre2, padre1)
        mutar(hijo1)
        mutar(hijo2)
        nuevaPoblacion.extend([hijo1, hijo2])

    poblacion = nuevaPoblacion

# ENCONTRAR LA MEJOR SOLUCION
mejorSolucion = max(poblacion, key=fitness)
mejorValor = fitness(mejorSolucion)
mejorPeso = sum(item["weight"] for i, item in enumerate(items) if mejorSolucion[i])

print("\nMejor solucion:", mejorSolucion)
print("Valor Total:", mejorValor)
print("Peso Total:", mejorPeso)


