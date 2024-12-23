import random
import itertools
from collections import defaultdict, deque

# Function to compute the load of reviewers based on the current assignment
def compute_load(assignments, M):
    load = [0] * (M + 1)
    for reviewers in assignments.values():
        for reviewer in reviewers:
            load[reviewer] += 1
    return load

# Function to calculate the maximum load from the load list
def max_load(load):
    return max(load)

# Function to initialize a random valid solution
def initialize_solution(N, M, b, preferences):
    assignments = {}
    for i in range(1, N + 1):
        assignments[i] = random.sample(preferences[i], b)
    return assignments

# Function to generate neighbors by swapping reviewers
def generate_neighbors(assignments, preferences, b, N):
    neighbors = []
    for i in range(1, N + 1):
        for j in range(b):
            for reviewer in preferences[i]:
                if reviewer not in assignments[i]:
                    new_assignment = assignments.copy()
                    new_assignment[i] = assignments[i][:]
                    new_assignment[i][j] = reviewer
                    neighbors.append(new_assignment)
    return neighbors

# Tabu Search Algorithm
def tabu_search(N, M, b, preferences, max_iterations=1000, tabu_tenure=7):
    # Initialize solution
    current_solution = initialize_solution(N, M, b, preferences)
    best_solution = current_solution
    current_load = compute_load(current_solution, M)
    best_load = max_load(current_load)

    # Tabu list
    tabu_list = deque(maxlen=tabu_tenure)

    for iteration in range(max_iterations):
        neighbors = generate_neighbors(current_solution, preferences, b, N)
        next_solution = None
        next_load_value = float('inf')

        for neighbor in neighbors:
            load = compute_load(neighbor, M)
            max_load_value = max_load(load)

            if neighbor not in tabu_list and max_load_value < next_load_value:
                next_solution = neighbor
                next_load_value = max_load_value

        if next_solution is not None:
            current_solution = next_solution
            tabu_list.append(next_solution)
            current_load = compute_load(current_solution, M)

            if max_load(current_load) < best_load:
                best_solution = current_solution
                best_load = max_load(current_load)

    return best_solution

# Input parsing
N, M, b = map(int, input().split())
preferences = {}

for i in range(1, N + 1):
    line = list(map(int, input().split()))
    k = line[0]
    preferences[i] = line[1:]

# Solve using Tabu Search
solution = tabu_search(N, M, b, preferences)

# Output results
print(N)
for i in range(1, N + 1):
    print(b, *solution[i])
