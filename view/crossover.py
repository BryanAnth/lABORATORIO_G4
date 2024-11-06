import random
from model.Chromosome import Chromosome

def crossover(parent1, parent2):
    # Verifica si el tamaño del path es suficiente para el crossover
    if len(parent1.path) <= 2 or len(parent2.path) <= 2:
        # Si el path es demasiado corto, devuelve los padres sin cambios
        return parent1, parent2

    # Selecciona un punto de cruce aleatorio dentro de un rango válido
    cross_point = random.randint(1, len(parent1.path) - 2)

    # Realiza el crossover en el punto de cruce
    offspring1_path = parent1.path[:cross_point] + parent2.path[cross_point:]
    offspring2_path = parent2.path[:cross_point] + parent1.path[cross_point:]

    offspring1_direction = parent1.direction[:cross_point] + parent2.direction[cross_point:]
    offspring2_direction = parent2.direction[:cross_point] + parent1.direction[cross_point:]

    offspring1_orientation = parent1.orientation[:cross_point] + parent2.orientation[cross_point:]
    offspring2_orientation = parent2.orientation[:cross_point] + parent1.orientation[cross_point:]

    # Crea los descendientes
    offspring1 = Chromosome(offspring1_path, offspring1_orientation, offspring1_direction)
    offspring2 = Chromosome(offspring2_path, offspring2_orientation, offspring2_direction)

    return offspring1, offspring2
