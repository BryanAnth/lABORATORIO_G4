import tkinter as tk
from model.Genetic_algorithm import GeneticAlgorithm
from model.Chromosome import Chromosome
from model.environment import create_environment
from utils.fitness import calculate_fitness
from view.visualization import draw_grid, draw_path

# Tamaño de cada celda en píxeles
CELL_SIZE = 40

def main():
    # Crear el entorno
    grid = create_environment(10, 10, obstacles=[(1, 0), (1, 1), (3, 4), (5, 6), (7, 2)])
    start = (0, 0)
    end = (9, 9)

    # Configurar la interfaz de tkinter
    root = tk.Tk()
    root.title("Visualización de Caminos con Tkinter")
    canvas = tk.Canvas(root, width=grid['size'][1] * CELL_SIZE, height=grid['size'][0] * CELL_SIZE)
    canvas.pack()

    # Dibujar el grid
    draw_grid(canvas, grid['size'], grid['obstacles'], start, end)

    # Generar caminos aleatorios
    cromosoma1 = Chromosome.random_chromosome(grid, start, end)
    # #Dibujarcaminos
    #draw_path(canvas, cromosoma1.path)
    test(cromosoma1)
    #draw_path(canvas, cromosoma2.path)

    ga = GeneticAlgorithm(grid, start, end, population_size=50, crossover_rate=0.7, mutation_rate=0.07, max_generations=30)
    best_solution = ga.run()
    draw_path(canvas, best_solution.path)
    
    print(f"fines  0 y 300 :{calculate_fitness(best_solution, ga.population)}")
    # Ejecutar la ventana de tkinter
    root.mainloop()



def test(cromosoma):
    print("Path")
    print(cromosoma.path)
    print("Direc")
    print(cromosoma.direction)
    print("Ori")
    print(cromosoma.orientation)
    print("FultPath")
    print(cromosoma.getPathFullUnitSteps())

if __name__ == "__main__":
    main()