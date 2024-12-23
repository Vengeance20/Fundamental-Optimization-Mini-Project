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

def greedy():
    cur = generate_initial_solution()
    while(True):
        ind = 0
        load = -9999999
        for i in range (M):
            tmp = 0
            for j in range(N):
                tmp += cur[j][i]
            if tmp >= load:
                load = tmp
                ind = i
                
        for i in range(N):
            if check_violation(cur[i]):
                if (cur[i][ind] == 1):
                    cur[i][ind] = 0

        if count_violations(cur) == 0:
            return cur

print(N)
best_solution = greedy()
for i in range(N):
    print(b, end = " ")
    for j in range(M):
        if best_solution[i][j] == 1:
            print(j + 1, end = " ")
    print()