import numpy as np

# Rastrigin function
def rastrigin(x):
    A = 10
    n = len(x)
    return A * n + sum([(xi**2 - A * np.cos(2 * np.pi * xi)) for xi in x])

# Initialize the population
def initialize_population(population_size, dimension):
    population = np.random.uniform(-5.12, 5.12, (population_size, dimension))
    return population

# Evaluate the fitness of individuals
def evaluate_fitness(population):
    return np.array([rastrigin(individual) for individual in population])

# Select parents using tournament selection
def tournament_selection(population, fitness, num_parents):
    selected_parents = []
    for _ in range(num_parents):
        indices = np.random.choice(len(population), size=2, replace=False)
        selected = population[indices[np.argmin(fitness[indices])]]
        selected_parents.append(selected)
    return np.array(selected_parents)

# Crossover (single-point crossover)
def crossover(parents, num_offsprings):
    offsprings = []
    for _ in range(num_offsprings):
        crossover_point = np.random.randint(1, len(parents[0]))
        parent1 = parents[np.random.randint(len(parents))]
        parent2 = parents[np.random.randint(len(parents))]
        offspring = np.hstack((parent1[:crossover_point], parent2[crossover_point:]))
        offsprings.append(offspring)
    return np.array(offsprings)

# Mutate offspring with a small probability
def mutate(offsprings, mutation_rate):
    mutated_offsprings = []
    for offspring in offsprings:
        if np.random.rand() < mutation_rate:
            mutation_point = np.random.randint(len(offspring))
            offspring[mutation_point] += np.random.uniform(-0.1, 0.1)
        mutated_offsprings.append(offspring)
    return np.array(mutated_offsprings)

# Main GA function
def genetic_algorithm(population_size, dimension, num_generations, num_parents, num_offsprings, mutation_rate):
    population = initialize_population(population_size, dimension)
    for generation in range(num_generations):
        fitness = evaluate_fitness(population)
        parents = tournament_selection(population, fitness, num_parents)
        offsprings = crossover(parents, num_offsprings)
        offsprings = mutate(offsprings, mutation_rate)
        population[:num_parents] = parents
        population[num_parents:] = offsprings
        best_fitness = min(fitness)
        print(f"Generation {generation}: Best Fitness = {best_fitness}")
    
    best_solution = population[np.argmin(fitness)]
    return best_solution, rastrigin(best_solution)

if __name__ == "__main__":
    population_size = 100
    dimension = 3
    num_generations = 100
    num_parents = 50
    num_offsprings = 50
    mutation_rate = 0.1

    best_solution, best_fitness = genetic_algorithm(population_size, dimension, num_generations, num_parents, num_offsprings, mutation_rate)
    print(f"Best Solution: {best_solution}")
    print(f"Best Fitness: {best_fitness}")
