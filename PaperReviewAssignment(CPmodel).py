from ortools.sat.python import cp_model

def assign_reviewers_optimized(N, M, b, L):
    model = cp_model.CpModel()

    # Decision variables: x[i][j] (1 if reviewer j is assigned to paper i)
    x = {}
    for i in range(N):
        for j in L[i]:
            x[i, j] = model.NewBoolVar(f'x[{i},{j}]')

    # Max load variable: maximum load of any reviewer
    max_load = model.NewIntVar(0, N, 'max_load')

    # Constraint 1: Each paper is reviewed by exactly b reviewers
    for i in range(N):
        model.Add(sum(x[i, j] for j in L[i]) == b)

    # Constraint 2: Max load of each reviewer
    for j in range(1, M + 1):
        model.Add(sum(x[i, j] for i in range(N) if j in L[i]) <= max_load)

    # Symmetry-breaking: Assign reviewers in increasing order
    for i in range(N):
        for k in range(len(L[i]) - 1):
            j1, j2 = L[i][k], L[i][k + 1]
            model.Add(x[i, j1] <= x[i, j2])

    # Minimize  max_load
    model.Minimize(max_load)

    all_vars = [x[i, j] for i in range(N) for j in L[i]]
    model.AddDecisionStrategy(all_vars, 
                               cp_model.CHOOSE_LOWEST_MIN, 
                               cp_model.SELECT_MIN_VALUE)

    # Solver
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(N)
        for i in range(N):
            reviewers = [j for j in L[i] if solver.Value(x[i, j]) == 1]
            print(b, *sorted(reviewers))
    else:
        print("No solution found.")

# Read input
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    N, M, b = map(int, data[0].split())
    L = [list(map(int, line.split()))[1:] for line in data[1:N + 1]]
    assign_reviewers_optimized(N, M, b, L)

if __name__ == "__main__":
    main()
