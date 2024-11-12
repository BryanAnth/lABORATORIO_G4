import random

class Chromosome:
    def __init__(self, path, orientation, direction):
        self.path = path               # Lista de coordenadas (x, y)
        self.orientation = orientation  # Lista de bits de orientación (0 = column-wise, 1 = row-wise)
        self.direction = direction      # Lista de bits de dirección (0 o 1, depende de orientation)

    def getPathFullUnitSteps(self):
        full_path = []
        full_path.append(self.path[0])
        for i in range(len(self.path) - 1):
            # Verificar que `self.orientation` y `self.direction` tienen el tamaño adecuado
            if i >= len(self.orientation) or i >= len(self.direction):
                print("Error: orientation o direction tienen un tamaño incorrecto.")
                break
            #Calculamos el desde el paso 1
            start = self.path[i]
            end = self.path[i + 1]
            orient = self.orientation[i]
            dir_first = self.direction[i]

            # Descomposición del movimiento en pasos unitarios
            if orient == 1:  # Row-wise
                if dir_first == 0:  # Primero en la dirección vertical
                    # Movimiento vertical
                    step_x =start[0] + 1
                    step_y = start[1]
                    full_path.append((step_x, step_y))

                    # Movimiento horizonral hacia end[1]
                    while step_y != end[1]:
                        step_y += 1 if end[1] > step_y else -1
                        full_path.append((step_x, step_y))

                else:  # Primero en la dirección horizontal
                    # Movimiento horizontal
                    step_x = start[0]
                    step_y = start[1]
                    while step_y != end[1]:
                        step_y += 1 if end[1] > step_y else -1
                        full_path.append((step_x, step_y))

                    # Movimiento vertical hacia end[0]
                    full_path.append((step_x + 1, step_y))

            else:  # Column-wise
                if dir_first == 0:  # Primero en la dirección horizontal
                    # Movimiento horizontal
                    step_x = start[0]
                    step_y = start[1]
                    while step_y != end[1]:
                        step_y += 1 if end[1] > step_y else -1
                        full_path.append((step_x, step_y))

                    # Movimiento vertical hacia end[0]
                    while step_x != end[0]:
                        step_x += 1 if end[0] > step_x else -1
                        full_path.append((step_x, step_y))

                else:  # Primero en la dirección vertical
                    # Movimiento vertical
                    step_x = start[0]
                    step_y = start[1]
                    while step_x != end[0]:
                        step_x += 1 if end[0] > step_x else -1
                        full_path.append((step_x, step_y))

                    # Movimiento horizontal hacia end[1]
                    while step_y != end[1]:
                        step_y += 1 if end[1] > step_y else -1
                        full_path.append((step_x, step_y))

        return full_path


    # Calcula el número de pasos no factibles en full_path
    def getFullPathInfeasibleSteps(self, grid):
        full_path = self.getPathFullUnitSteps()
        infeasible_steps = sum(1 for step in full_path if step in grid['obstacles'])
        return infeasible_steps

    # Calcula la longitud total del full_path
    def getFullPathLength(self):
        full_path = self.getPathFullUnitSteps()
        return len(full_path)

    # Calcula el número de giros (turns) en el camino (no en full_path)
    def getFullPathTurns(self):
        return len(self.path) - 1

    @staticmethod
    def random_chromosome(grid, start, end):
        path = [start]
        orientation = []
        direction = []
        steps = 0  # Contador de pasos
        max_steps = grid['max_steps']
        
        while path[-1] != end and steps < max_steps:
            print(f"Step {steps}: Current position {path[-1]}, trying to reach {end}")
            # Elegir orientación aleatoriamente
            current_orientation = random.choice([0, 1])  # 0 = Column-wise, 1 = Row-wise
            current_direction = random.choice([0, 1])  # 0 = Primero vertical, 1 = Primero horizontal
            
            # Obtener la última coordenada en el camino
            current_x, current_y = path[-1]
            
            # Generar el siguiente paso basado en la orientación
            if current_orientation == 1:  # Row-wise
                next_x = current_x + 1 
                next_y = random.randint(0, grid['size'][1] - 1)

            else:  # Column-wise
                next_x = random.randint(0, grid['size'][0] - 1)
                next_y = current_y + 1 

            # Asegurarse de que el siguiente paso esté dentro de los límites y no sea un obstáculo
            if (0 <= next_x < grid['size'][0] and 0 <= next_y < grid['size'][1] and
                    (next_x, next_y) not in path and (next_x, next_y) not in grid['obstacles']):
                # print(path[-1])
                orientation.append(current_orientation)
                direction.append(current_direction)
                path.append((next_x, next_y))

            steps += 1
        
        return Chromosome(path, orientation, direction)
    