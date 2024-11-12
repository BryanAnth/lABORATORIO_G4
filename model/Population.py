from model.Chromosome import Chromosome

class Population:
    def __init__(self, 
                grid, start, end, population_size):
        self.grid = grid
        self.start = start
        self.end = end
        self.population_size = population_size
        self.population = [Chromosome.random_chromosome(grid, start, end) for _ in range(population_size)]
    
    #Population Infeasible
    # Mínimo número de pasos no factibles (en obstáculos) en la población
    def getMinPathInfeasibleSteps(self):
        min_infeasible_steps = float('inf')
        
        for chromosome in self.population:
            infeasible_steps = chromosome.getFullPathInfeasibleSteps(self.grid)
            min_infeasible_steps = min(min_infeasible_steps, infeasible_steps)
        
        return min_infeasible_steps

    # Máximo número de pasos no factibles (en obstáculos) en la población
    def getMaxPathInfeasibleSteps(self):
        max_infeasible_steps = float('-inf')
        
        for chromosome in self.population:
            infeasible_steps = chromosome.getFullPathInfeasibleSteps(self.grid)
            max_infeasible_steps = max(max_infeasible_steps, infeasible_steps)
        
        return max_infeasible_steps
    
    #Pop Length
    # Mínimo número de pasos en el full_path (longitud) en la población
    def getMinPathLength(self):
        min_path_length = float('inf')
        
        for chromosome in self.population:
            path_length = chromosome.getFullPathLength()
            min_path_length = min(min_path_length, path_length)
        
        return min_path_length

    # Máximo número de pasos en el full_path (longitud) en la población
    def getMaxPathLength(self):
        max_path_length = float('-inf')
        
        for chromosome in self.population:
            path_length = chromosome.getFullPathLength()
            max_path_length = max(max_path_length, path_length)
        
        return max_path_length

    #Pop Turns
    # Mínimo número de giros en la población
    def getMinPathTurns(self):
        min_turns = float('inf')
        
        for chromosome in self.population:
            turns = chromosome.getFullPathTurns()
            min_turns = min(min_turns, turns)
        
        return min_turns

    # Máximo número de giros en la población
    def getMaxPathTurns(self):
        max_turns = float('-inf')
        
        for chromosome in self.population:
            turns = chromosome.getFullPathTurns()
            max_turns = max(max_turns, turns)
        
        return max_turns
    
