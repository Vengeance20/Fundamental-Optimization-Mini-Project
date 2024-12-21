import sys

[N, M, b] = [int(x) for x in sys.stdin.readline().split()]
lst = dict()
for i in range(N):
    lst[i + 1] = [int(x) for x in sys.stdin.readline().split()]


def generate_initial_solution():
    #Using reviewers' preferences to generate initial solution
    P = [[0 for i in range(M)] for j in range(N)]
    for i in range(N):
        for k in range(1, len(lst[i + 1])):
            P[i][lst[i + 1][k] - 1] = 1
    return P

def calculate_max_load(cur):
    load = -9999999
    for i in range (M):
        tmp = 0
        for j in range(N):
            tmp += cur[j][i]
        if tmp > load:
            load = tmp
    return load

def check_violation(reviewer_list):
    no_of_reviewers = 0
    for i in range(len(reviewer_list)):
        no_of_reviewers += reviewer_list[i]
    if (no_of_reviewers > b):
        return True
    return False

def count_violations(cur):
    violations = 0
    for reviewer_list in cur:
        if check_violation(reviewer_list):
            violations += 1
    return violations
    
def generate_neighbors(cur):
    neighbors = []
    ind = 0
    load = -9999999
    for i in range (M):
        tmp = 0
        for j in range(N):
            tmp += cur[j][i]
        if tmp > load:
            load = tmp
            ind = i
    
    for i in range(N):
        if check_violation(cur[i]):
            if (cur[i][ind] == 1):
                neighbor = cur[:]
                neighbor[i][ind] = 0
                neighbors.append(neighbor)

    return neighbors

def local_search(max_iterations = 1000):
    current_solution = generate_initial_solution()
    current_violations = count_violations(current_solution)
    current_max_load = calculate_max_load(current_solution)
    minimal_max_load = current_max_load

    for i in range(max_iterations):
        neighbors = generate_neighbors(current_solution)
        for neighbor in neighbors:
            violations = count_violations(neighbor)
            max_load = calculate_max_load(neighbor)
            if violations < current_violations or max_load < minimal_max_load:
                minimal_max_load = max_load
                current_violations = violations
                current_solution = neighbor
        
    return current_solution

print(N)
best_solution = local_search()
for i in range(N):
    print(b, end = " ")
    for j in range(M):
        if best_solution[i][j] == 1:
            print(j + 1, end = " ")
    print()

print(calculate_max_load(best_solution))
