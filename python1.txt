# Function to perform union of two fuzzy sets
def fuzzy_union(setA, setB):
    return {x: max(setA.get(x, 0), setB.get(x, 0)) for x in set(setA) | set(setB)}

# Function to perform intersection of two fuzzy sets
def fuzzy_intersection(setA, setB):
    return {x: min(setA.get(x, 0), setB.get(x, 0)) for x in set(setA) & set(setB)}

# Function to perform complement of a fuzzy set
def fuzzy_complement(fuzzy_set):
    return {x: 1 - mu for x, mu in fuzzy_set.items()}

# Function to perform Cartesian product of two fuzzy sets
def cartesian_product(setA, setB):
    return {(a, b): min(setA[a], setB[b]) for a in setA for b in setB}

# Function to perform max-min composition of two fuzzy relations
def max_min_composition(relation1, relation2):
    result = {}
    for (a, b1), mu1 in relation1.items():
        for (b2, c), mu2 in relation2.items():
            if b1 == b2:  # Ensure relations match
                key = (a, c)
                if key not in result:
                    result[key] = 0
                result[key] = max(result[key], min(mu1, mu2))
    return result

# Example Usage
if __name__ == "__main__":
    # Define two fuzzy sets A and B
    fuzzy_set_A = {'x1': 0.2, 'x2': 0.3, 'x3': 0.5}
    fuzzy_set_B = {'y1': 0.8, 'y2': 0.6,'y3':0.3}

    print("Fuzzy Set A:", fuzzy_set_A)
    print("Fuzzy Set B:", fuzzy_set_B)

    # Mathematical operations
    union_result = fuzzy_union(fuzzy_set_A, fuzzy_set_B)
    intersection_result = fuzzy_intersection(fuzzy_set_A, fuzzy_set_B)
    complement_A = fuzzy_complement(fuzzy_set_A)

    print("\nUnion of A and B:", union_result)
    print("Intersection of A and B:", intersection_result)
    print("Complement of A:", complement_A)

    # Cartesian Product
    relation_R = cartesian_product(fuzzy_set_A, fuzzy_set_B)
    print("\nCartesian Product (Fuzzy Relation R):")
    for pair, mu in relation_R.items():
        print(f"{pair}: {mu}")

    # Define another relation S for max-min composition
    fuzzy_set_C = {'z1': 0.6, 'z2': 0.9}
    relation_S = cartesian_product(fuzzy_set_B, fuzzy_set_C)
    print("\nFuzzy Relation S:")
    for pair, mu in relation_S.items():
        print(f"{pair}: {mu}")

    # Max-Min Composition
    composition_result = max_min_composition(relation_R, relation_S)
    print("\nMax-Min Composition of R and S:")
    for pair, mu in composition_result.items():
        print(f"{pair}: {mu}")
    # R_dict = {('A', 'X'): 0.2, ('A', 'Y'): 0.5, ('A', 'Z'): 0.7,
    #       ('B', 'X'): 0.4, ('B', 'Y'): 0.6, ('B', 'Z'): 0.8}
    
    # S_dict = {('X', 'P'): 0.5, ('X', 'Q'): 0.9, 
    #       ('Y', 'P'): 0.1, ('Y', 'Q'): 0.6,
    #       ('Z', 'P'): 0.4, ('Z', 'Q'): 0.3}
    R_dict = {
    ('A', 'X'): 0.6,  # Relation between A and X with degree 0.6
    ('A', 'Y'): 0.3,  # Relation between A and Y with degree 0.3
    ('B', 'X'): 0.2,  # Relation between B and X with degree 0.2
    ('B', 'Y'): 0.9   # Relation between B and Y with degree 0.9
    }

    S_dict = {
    ('X', 'P'): 1.0,  # Relation between X and P with degree 1.0
    ('X', 'Q'): 0.5,  # Relation between X and Q with degree 0.5
    ('X', 'R'): 0.3,  # Relation between X and R with degree 0.3
    ('Y', 'P'): 0.8,  # Relation between Y and P with degree 0.8
    ('Y', 'Q'): 0.4,  # Relation between Y and Q with degree 0.4
    ('Y', 'R'): 0.7   # Relation between Y and R with degree 0.7
    }


    
    T = max_min_composition(R_dict, S_dict)

    # Print the resulting fuzzy relation
    T = max_min_composition(R_dict, S_dict)

    # Print the resulting fuzzy relation
    print("\nResulting Fuzzy Relation T (Max-Min Composition):")
    print(T)
