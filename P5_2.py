import numpy as np
import random

# Define the distance matrix
M = 2 * np.ones([11, 11])
M[1][3] = 1
M[3][5] = 1
M[5][7] = 1
M[7][9] = 1
M[9][2] = 1
M[2][4] = 1
M[4][6] = 1
M[6][8] = 1
M[8][10] = 1

print(M)

# Define parameters
num_cities = 10
population_size = 10
num_generations = 100
mutation_rate = 0.02

# Create a function to calculate the total distance of a route
def calculate_total_distance(route):
    total_distance = 0
    for i in range(num_cities - 1):
        total_distance += M[route[i]][route[i + 1]]
    total_distance += M[route[-1]][route[0]]  # Return to the starting city
    return total_distance

# Create an initial population of random routes
population = [list(range(1, num_cities + 1)) for _ in range(population_size)]

# Main GA loop
for generation in range(num_generations):
    # Evaluate fitness of each route
    fitness_scores = [1 / calculate_total_distance(route) for route in population]
    
    # Select parents using roulette wheel selection
    parents = random.choices(population, weights=fitness_scores, k=population_size)
    
    # Create the next generation using ordered crossover
    new_population = []
    for _ in range(0, population_size, 2):
        parent1, parent2 = random.sample(parents, 2)
        crossover_point = random.randint(1, num_cities - 1)
        child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[crossover_point:]]
        child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[crossover_point:]]
        new_population.extend([child1, child2])
    
    # Apply mutation
    for i in range(population_size):
        if random.random() < mutation_rate:
            j, k = random.sample(range(num_cities), 2)
            new_population[i][j], new_population[i][k] = new_population[i][k], new_population[i][j]
    
    # Update the population
    population = new_population

# Find the best route in the final population
best_route = min(population, key=calculate_total_distance)
best_distance = calculate_total_distance(best_route)

print("Best Route:", best_route)
print("Total Distance:", best_distance)

