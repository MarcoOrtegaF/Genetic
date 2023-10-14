import numpy as np
import random

# Define the Ackley function
def ackley(x, y):
    a = 20
    b = 0.2
    c = 2 * np.pi
    return -a * np.exp(-b * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(c * x) + np.cos(c * y))) + a + np.exp(1)

# Genetic Algorithm parameters
population_size = 100
num_generations = 100
mutation_rate = 0.1

# Define the initial population
def initialize_population(size):
    return [(random.uniform(-5, 5), random.uniform(-5, 5)) for _ in range(size)]

# Calculate the fitness of each individual
def calculate_fitness(individual):
    x, y = individual
    return ackley(x, y)

# Select parents for reproduction using tournament selection
def tournament_selection(population, k=5):
    tournament = random.sample(population, k)
    return min(tournament, key=calculate_fitness)

# Crossover (single-point crossover in this example)
def crossover(parent1, parent2):
    x1, y1 = parent1
    x2, y2 = parent2
    crossover_point = random.randint(0, 1)
    if crossover_point == 0:
        return (x1, y2)
    else:
        return (x2, y1)

# Mutate an individual
def mutate(individual, mutation_rate):
    x, y = individual
    if random.random() < mutation_rate:
        return (x + random.uniform(-0.1, 0.1), y + random.uniform(-0.1, 0.1))
    else:
        return individual

# Main GA loop
population = initialize_population(population_size)

for generation in range(num_generations):
    population = sorted(population, key=calculate_fitness)
    new_population = []

    # Elitism: Keep the best individual
    new_population.append(population[0])

    # Create the next generation
    while len(new_population) < population_size:
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        child = crossover(parent1, parent2)
        child = mutate(child, mutation_rate)
        new_population.append(child)

    population = new_population

best_solution = population[0]
best_fitness = calculate_fitness(best_solution)

print(f"Best solution: {best_solution}")
print(f"Best fitness: {best_fitness}")
