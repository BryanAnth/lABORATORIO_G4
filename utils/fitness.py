def calculate_fitness(chromosome, population, w_f=3, w_l=2, w_t=2):
    # Obtener los valores específicos del cromosoma
    S = chromosome.getFullPathInfeasibleSteps(population.grid)  # Número de pasos no factibles del cromosoma
    L = chromosome.getFullPathLength()  # Longitud total del camino del cromosoma
    T = chromosome.getFullPathTurns()   # Número de giros en el camino del cromosoma

    # Obtener los valores mínimos y máximos de la población
    S_min = population.getMinPathInfeasibleSteps()
    S_max = population.getMaxPathInfeasibleSteps()

    L_min = population.getMinPathLength()
    L_max = population.getMaxPathLength()

    T_min = population.getMinPathTurns()
    T_max = population.getMaxPathTurns()

    # Calcular los factores normalizados
    if S_max > S_min:
        f_f = 1 - (S - S_min) / (S_max - S_min)
    else:
        f_f = 1  # Si todos los cromosomas tienen el mismo número de pasos no factibles

    if L_max > L_min:
        f_l = 1 - (L - L_min) / (L_max - L_min)
    else:
        f_l = 1  # Si todos los cromosomas tienen el mismo camino

    if T_max > T_min:
        f_t = 1 - (T - T_min) / (T_max - T_min)
    else:
        f_t = 1  # Si todos los cromosomas tienen el mismo número de giros

    # Calcular el valor de fitness total
    fitness = 100 * w_f * f_f * ((w_l * f_l + w_t * f_t) / (w_l + w_t))
    
    return fitness

