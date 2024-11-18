
# Genetic Algorithm for Autonomous Robot Navigation

This repository implements a **Genetic Algorithm (GA)** to solve the problem of autonomous robot navigation in a grid-based environment. The main objective is to compute the shortest feasible path from a starting point to an endpoint, avoiding obstacles, while optimizing path length, feasibility, and turns.

The project is inspired by research on genetic algorithms applied to robot path planning and adapts their principles to a modular Python implementation.

---

## Features

- **Path Representation**: Chromosomes represent robot paths through a grid.
- **Fitness Evaluation**: Optimizes feasibility, path length, and turns using a weighted fitness function.
- **Crossover**: Combines parent chromosomes to generate new paths with single-point crossover.
- **Mutation**: Introduces diversity by randomly altering genes in a chromosome.
- **Elitism**: Retains the best solution in each generation to ensure progress.

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
