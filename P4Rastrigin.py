import random
import math

class Chromosome:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.fitness = self.evaluate()

    def evaluate(self):
        # Calculate the Rastrigin function in 3 dimensions
        fitness = 10 * 3 - 10 * (cos(2 * math.pi * self.x) + cos(2 * math.pi * self.y) + cos(2 * math.pi * self.z)) + (self.x**2 + self.y**2 + self.z**2)
        return fitness

class Population:
    def __init__(self, population_size):
        self.chromosomes = []
        for i in range(population_size):
            # Generate a random chromosome
            x = random.uniform(-5.12, 5.12)
            y = random.uniform(-5.12, 5.12)
            z = random.uniform(-5.12, 5.12)
            chromosome = Chromosome(x, y, z)
            self.chromosomes.append(chromosome)

    def sort(self):
        # Sort the chromosomes by fitness, in ascending order
        self.chromosomes.sort(key=lambda chromosome: chromosome.fitness)

    def select(self, selection_pressure):
        # Select the top chromosomes based on their fitness
        selected_chromosomes = []
        for i in range(selection_pressure):
            selected_chromosomes.append(self.chromosomes[i])
        return selected_chromosomes

    def crossover(self, selected_chromosomes, crossover_rate):
        # Crossover the selected chromosomes to produce new offspring
        offspring = []
        for i in range(0, len(selected_chromosomes) - 1, 2):
            # Generate a random crossover point
            crossover_point = random.randint(0, len(selected_chromosomes[0].x) - 1)

            # Offspring 1
            offspring_1 = Chromosome(selected_chromosomes[i].x[0:crossover_point] + selected_chromosomes[i + 1].x[crossover_point:], selected_chromosomes[i].y[0:crossover_point] + selected_chromosomes[i + 1].y[crossover_point:], selected_chromosomes[i].z[0:crossover_point] + selected_chromosomes[i + 1].z[crossover_point:])

            # Offspring 2
            offspring_2 = Chromosome(selected_chromosomes[i + 1].x[0:crossover_point] + selected_chromosomes[i].x[crossover_point:], selected_chromosomes[i + 1].y[0:crossover_point] + selected_chromosomes[i].y[crossover_point:], selected_chromosomes[i + 1].z[0:crossover_point] + selected_chromosomes[i].z[crossover_point:])

            # Add the offspring to the population
            offspring.append(offspring_1)
            offspring.append(offspring_2)

        return offspring

    def mutate(self, offspring, mutation_rate):
        # Mutate the offspring with a given probability
        for chromosome in offspring:
            for i in range(len(chromosome.x)):
                if random.random() < mutation_rate:
                    # Mutate the gene
                    chromosome.x[i] += random.uniform(-0.1, 0.1)
                    chromosome.y[i] += random.uniform(-0.1, 0.1)
                    chromosome.z[i] += random.uniform(-0.1, 0.1)

        return offspring

def run_ga(population_size, selection_pressure, crossover_rate, mutation_rate, max_iterations):
    # Create an initial population
    population = Population(population_size)

    # Iterate over the generations
    for i in range(max_iterations):
        # Evaluate the fitness of each chromosome
        population.sort()

        # Select the top chromosomes based on their fitness
        selected_chromosomes = population.select(selection_pressure)

        # Crossover the selected chromosomes to produce new offspring
