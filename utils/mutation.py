import random

def mutate(chromosome, grid):
    # Selecciona un punto de mutación aleatorio en el camino
    mutation_point = random.randint(1, len(chromosome.path) - 1)  # Empieza desde 1 para asegurar que haya un paso anterior

    # Asegurarse de que mutation_point - 1 esté dentro del rango de orientation
    if mutation_point - 1 >= len(chromosome.orientation):
        print("Error: mutation_point - 1 está fuera del rango de orientation.")
        return  # Salir de la función si hay un error en el tamaño

    # Obtiene la orientación del paso anterior
    previous_orientation = chromosome.orientation[mutation_point - 1]

    # Obtiene la posición actual del punto de mutación
    current_step = chromosome.path[mutation_point]

    # Genera el nuevo paso basado en la orientación del paso anterior
    if previous_orientation == 1:  # Row-wise
        # Mantiene la columna y cambia solo la fila dentro de los límites
        new_step = (random.randint(0, grid['size'][0] - 1), current_step[1])
    else:  # Column-wise
        # Mantiene la fila y cambia solo la columna dentro de los límites
        new_step = (current_step[0], random.randint(0, grid['size'][1] - 1))

    # Actualiza el punto de mutación con el nuevo paso y cambia la dirección
    chromosome.path[mutation_point] = new_step
    # Asegúrate de que `direction` tenga el tamaño adecuado antes de asignar el valor
    if mutation_point < len(chromosome.direction):
        chromosome.direction[mutation_point] = random.choice([0, 1])
    else:
        # Si el índice no existe, agrega el valor al final
        chromosome.direction.append(random.choice([0, 1]))