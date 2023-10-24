import random


# DEFINIR LAS CIUDADES COMO COORDENADAS X, Y
ciudades = [(1, 3), (3, 5), (5, 7), (7, 9), (9, 2), (2, 4), (4, 6), (6, 8), (8, 10)]

# DEFINIMOS LOS VALORES DEL ALGORITMO
tamPoblacion = 250
numgenraciones = 500

# Define the mutation rate
tasaMutacion = 0.8

# FUNCION PARA CALCULAR LA DISTANCIA TOTAL DE LA RUTA
def distanciaTotal(ruta):
    distancia = 0
    for i in range(len(ruta) - 1):
        x1, y1 = ciudades[ruta[i]]
        x2, y2 = ciudades[ruta[i + 1]]
        distancia += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distancia

# CREAR UNA POBLACION INICIAL DE RUTAS
def InicPoblacion(tamPoblacion):
    poblacion = []
    for _ in range(tamPoblacion):
        ruta = list(range(len(ciudades)))
        random.shuffle(ruta)
        poblacion.append(ruta)
    return poblacion

# MUTAR LA RUTA
def mutar(ruta):
    for i in range(len(ruta)):
        if random.random() < tasaMutacion:
            j = random.randint(0, len(ruta) - 1)
            ruta[i], ruta[j] = ruta[j], ruta[i]
    return ruta

# SELECCIONAR DOS PADRES DE LA POBLACION MEDIANTE UN TORNEO
def selPadres(poblacion):
    tamTorneo = 5
    candidatos = random.sample(poblacion, tamTorneo)
    candidatos.sort(key=lambda ruta: distanciaTotal(ruta))
    return candidatos[0], candidatos[1]

# CCREAMOS NUEVAS RUTAS CON EL CROSSOVER
def crossover(padre1, padre2):
    puntoCross = random.randint(0, len(padre1) - 1)
    hijo = padre1[:puntoCross]
    for gen in padre2:
        if gen not in hijo:
            hijo.append(gen)
    return hijo

# CICLO PRINCIPAL DEGL GA
poblacion = InicPoblacion(tamPoblacion)

for generacion in range(numgenraciones):
    poblacion.sort(key=lambda ruta: distanciaTotal(ruta))
    mejorRuta = poblacion[0]
    print(f"generacion {generacion}: Best distancia = {distanciaTotal(mejorRuta)}")

    nuevaPoblacion = [mejorRuta]

    while len(nuevaPoblacion) < tamPoblacion:
        padre1, padre2 = selPadres(poblacion)
        hijo = crossover(padre1, padre2)
        hijo = mutar(hijo)
        nuevaPoblacion.append(hijo)

    poblacion = nuevaPoblacion

mejorRuta = poblacion[0]
print("Best ruta:", mejorRuta)
print("Best distancia:", distanciaTotal(mejorRuta))
