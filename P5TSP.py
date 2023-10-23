import random
import numpy as np

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class TSP:
    def __init__(self, cities):
        self.cities = cities
        self.tour = random.sample(self.cities, len(self.cities))

    def fitness(self):
        total_distance = 0
        for i in range(len(self.tour) - 1):
            total_distance += self.tour[i].distance(self.tour[i + 1])
        total_distance += self.tour[-1].distance(self.tour[0])
        return total_distance

    def crossover(self, other):
        child = TSP([])
        for i in range(len(self.tour)):
            if random.random() < 0.5:
                child.tour.append(self.tour[i])
            else:
                child.tour.append(other.tour[i])
        return child

    def mutate(self):
        i = random.randint(0, len(self.tour) - 1)
        j = random.randint(0, len(self.tour) - 1)
        self.tour[i], self.tour[j] = self.tour[j], self.tour[i]

def genetic_algorithm(cities, population_size, generations):
    population = []
    for i in range(population_size):
        population.append(TSP(cities))

    best_tour = population[0]
    for i in range(generations):
        new_population = []
        for j in range(0, population_size, 2):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = parent1.crossover(parent2)
            child.mutate()
            new_population.append(child)

        population = new_population
        best_tour = min(population, key=lambda tour: tour.fitness())

    return best_tour

def main():
    cities = [City(1, 2), City(3, 4), City(5, 6), City(7, 8), City(9, 10)]
    best_tour = genetic_algorithm(cities, 100, 100)

    print("Best tour:")
    for city in best_tour.tour:
        print(city.x, city.y)

    print("Total distance:", best_tour.fitness())

if __name__ == "__main__":
    main()
