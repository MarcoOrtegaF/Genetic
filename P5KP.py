import random

def generate_population(population_size):

    population = []
    for i in range(population_size):
        solution = []
        for item in items:
            if random.random() < 0.5:
                solution.append(1)
            else:
                solution.append(0)
        population.append(solution)

    return population


def evaluate_solution(solution):

    fitness = 0
    weight = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            fitness += items[i][0]
            weight += items[i][1]
    if weight <= capacity:
        return fitness
    else:
        return 0


def crossover(solution1, solution2):

    crossover_point = random.randint(0, len(solution1) - 1)
    child1 = solution1[:crossover_point] + solution2[crossover_point:]
    child2 = solution2[:crossover_point] + solution1[crossover_point:]

    return child1, child2


def mutate(solution):

    mutation_point = random.randint(0, len(solution) - 1)
    solution[mutation_point] = 1 - solution[mutation_point]

    return solution


def solve(population_size, generations):

    population = generate_population(population_size)
    best_solution = None
    best_fitness = 0

    for i in range(generations):
        new_population = []
        for j in range(0, population_size, 2):
            child1, child2 = crossover(population[j], population[j + 1])
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.append(child1)
            new_population.append(child2)

        population = new_population

        for solution in population:
            fitness = evaluate_solution(solution)
            if fitness > best_fitness:
                best_solution = solution
                best_fitness = fitness

    return best_solution, best_fitness


if __name__ == '__main__':
    items = [(1, 2), (2, 2), (3, 4), (4, 5), (6, 5), (7, 6), (9, 7)]
    capacity = 10

    best_solution, best_fitness = solve(100, 200)

    print("Best solution:", best_solution)
    print("Best fitness:", best_fitness)
