import random

# Parameters
TARGET_WORD = "evolution"  # The target word to match
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
GENERATIONS = 1000
CHARACTER_SET = 'abcdefghijklmnopqrstuvwxyz'

def random_word(length):
    """Generate a random word of a specified length."""
    return ''.join(random.choice(CHARACTER_SET) for _ in range(length))

def fitness(candidate):
    """Calculate fitness as the number of matching characters with the target word."""
    return sum(1 for a, b in zip(candidate, TARGET_WORD) if a == b)

def select_parents(population):
    """Select two parents based on fitness proportional selection."""
    weights = [fitness(word) for word in population]
    total_fitness = sum(weights)
    probabilities = [weight / total_fitness for weight in weights]
    parent1 = random.choices(population, probabilities)[0]
    parent2 = random.choices(population, probabilities)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    """Perform crossover between two parents to create a child."""
    crossover_point = random.randint(1, len(TARGET_WORD) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(word):
    """Mutate a word by randomly changing one character."""
    if random.random() < MUTATION_RATE:
        index = random.randint(0, len(word) - 1)
        new_char = random.choice(CHARACTER_SET)
        word = word[:index] + new_char + word[index + 1:]
    return word

def genetic_algorithm():
    """Run the Genetic Algorithm to evolve a word toward the target."""
    # Initialize population
    population = [random_word(len(TARGET_WORD)) for _ in range(POPULATION_SIZE)]

    for generation in range(GENERATIONS):
        # Evaluate fitness
        population = sorted(population, key=fitness, reverse=True)

        # Check if we found the target word
        if fitness(population[0]) == len(TARGET_WORD):
            print(f"Target word '{TARGET_WORD}' found in generation {generation}!")
            return population[0]

        # Create new population
        new_population = []

        # Elitism: keep the best word
        new_population.append(population[0])

        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = select_parents(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

        # Print the best candidate in this generation
        best_candidate = population[0]
        print(f"Generation {generation}: Best candidate = '{best_candidate}', Fitness = {fitness(best_candidate)}")

    print("Reached the maximum number of generations.")

# Run the Genetic Algorithm
if __name__ == "__main__":
    genetic_algorithm()

