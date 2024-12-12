import random
import numpy as np
from sklearn import datasets
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from deap import base, creator, tools, algorithms

# Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Define the fitness function
def svm_fitness(individual):
    C = max(individual[0], 0.0001)  # Ensure C is positive
    gamma = max(individual[1], 0.0001)  # Ensure gamma is positive
    # Define the model with current hyperparameters
    model = SVC(C=C, gamma=gamma)
    # Perform cross-validation
    accuracy = cross_val_score(model, X, y, cv=5).mean()
    return accuracy,

# Create the fitness function and individual (chromosome) structure
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# Define the parameter space (e.g., C and gamma)
toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, 0.0, 100)  # C: 0.1 to 100
toolbox.register("attr_float2", random.uniform, 0.0001, 1)  # gamma: 0.0001 to 1

# Structure of an individual
toolbox.register("individual", tools.initCycle, creator.Individual,
                 (toolbox.attr_float, toolbox.attr_float2), n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Register genetic algorithm operations
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", svm_fitness)

# Run the genetic algorithm
def main():
    pop = toolbox.population(n=20)  # Population size
    hof = tools.HallOfFame(1)       # Hall of Fame to store the best individual
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("max", np.max)

    # Use the algorithm.eaSimple method for evolution
    algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=20,  # 20 generations
                        stats=stats, halloffame=hof, verbose=True)

    print("Best individual: ", hof[0])
    print("Best fitness: ", hof[0].fitness.values[0])

if __name__ == "__main__":
    main()
