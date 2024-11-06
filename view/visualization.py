# Tamaño de cada celda en píxeles
CELL_SIZE = 40

def draw_grid(canvas, grid_size, obstacles, start, end):
    # Dibujar el grid
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            x1, y1 = j * CELL_SIZE, i * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
            color = "white"  # Color de fondo para las celdas

            # Pintar obstáculos
            if (i, j) in obstacles:
                color = "black"
            # Pintar punto de inicio
            elif (i, j) == start:
                color = "green"
            # Pintar punto final
            elif (i, j) == end:
                color = "red"

            # Dibujar el rectángulo de la celda
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

def draw_path(canvas, path):
    # Dibujar el camino en el grid
    for i in range(len(path) - 1):
        x1, y1 = path[i][1] * CELL_SIZE + CELL_SIZE // 2, path[i][0] * CELL_SIZE + CELL_SIZE // 2
        x2, y2 = path[i + 1][1] * CELL_SIZE + CELL_SIZE // 2, path[i + 1][0] * CELL_SIZE + CELL_SIZE // 2
        # Dibujar una línea entre los puntos del camino
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)
