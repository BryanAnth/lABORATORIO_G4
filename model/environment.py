def create_environment(rows, cols, obstacles):
    max_steps = rows * cols - len(obstacles)
    
    grid = {'size': (rows, cols), 'obstacles': set(obstacles), 'max_steps': max_steps}
    return grid