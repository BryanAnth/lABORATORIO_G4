def create_environment(rows, cols, obstacles):
    grid = {'size': (rows, cols), 'obstacles': set(obstacles)}
    return grid