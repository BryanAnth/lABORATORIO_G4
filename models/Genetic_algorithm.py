from model.Chromosome import Chromosome
from model.Population import Population
from utils.crossover import crossover #crossover(parent1, parent2)
from utils.fitness import calculate_fitness #calculate_fitness(chromosome, population, w_f=3, w_l=2, w_t=2):
from utils.mutation import mutate #mutate(chromosome, grid):

import random

class GeneticAlgorithm:
    def __init__(self, 
                grid, start, end, population_size, crossover_rate, mutation_rate, max_generations):
        self.grid = grid
        self.start = start
        self.end = end
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations
        self.population = Population(grid, start, end, population_size)

    def run(self):
        best_solution = None
        best_fitness = float('-inf')

        for generation in range(self.max_generations):
            next_generation = []

            # Calcular el fitness de cada cromosoma en la población actual
            fitness_scores = []
            for chromosome in self.population.population:
                fitness = calculate_fitness(chromosome, self.population)
                fitness_scores.append(fitness)

                # Verificar si es el mejor cromosoma hasta el momento
                if fitness > best_fitness:
                    best_fitness = fitness
                    best_solution = chromosome

            # Agregar el mejor cromosoma (elitismo) a la próxima generación
            next_generation.append(best_solution)

            # Seleccionar cromosomas para crossover
            crossover_candidates = [
                chromosome for chromosome, fitness in zip(self.population.population, fitness_scores)
                if random.random() < self.crossover_rate
            ]

            # Aplicar crossover y agregar descendientes a la próxima generación
            while len(next_generation) < int(self.population_size * 0.9):  # Rellenamos el 90% con crossover
                if len(crossover_candidates) >= 2:
                    parent1, parent2 = random.sample(crossover_candidates, 2)
                    offspring1, offspring2 = crossover(parent1, parent2)
                    next_generation.extend([offspring1, offspring2])

            # Aplicar mutación a un 7% de la población restante
            mutation_candidates = [
                chromosome for chromosome in self.population.population
                if chromosome not in next_generation and random.random() < self.mutation_rate
            ]

            for chromosome in mutation_candidates:
                mutate(chromosome, self.grid)
                next_generation.append(chromosome)

            # Si aún falta llenar la población, completamos con nuevos cromosomas aleatorios
            while len(next_generation) < self.population_size:
                next_generation.append(Chromosome.random_chromosome(self.grid, self.start, self.end))

            # Actualizamos la población con la próxima generación
            self.population.population = next_generation

        return best_solution
