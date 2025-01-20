from ortools.linear_solver import pywraplp
import sys

#data
[N, M, b] = [int(x) for x in sys.stdin.readline().split()]
lst = dict()
for i in range(N):
    lst[i + 1] = [int(x) for x in sys.stdin.readline().split()]

P = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    for k in range(1, len(lst[i + 1])):
        P[i][lst[i + 1][k] - 1] = 1

def main():
    solver = pywraplp.Solver.CreateSolver("SCIP")
    if not solver:
        return

    #define variables
    x = {}
    for i in range(1, N + 1):
        x[i] = {}
        for j in range(1, M + 1):
            x[i][j] = solver.IntVar(0, 1, "x[%a][%a]" % (i , j))

    y = {}
    for i in range(1, N + 1):
        y[i] = solver.IntVar(0, N, "y[%a]" % i)

    Z = solver.IntVar(0, N, "Z")


    #Add constraints
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            y[i] += x[j][i]
        solver.Add(Z >= y[i])

    for i in range(1, N + 1):
        reviewers_per_paper = [x[i][j] for j in range(1, M + 1)]
        solver.Add(sum(reviewers_per_paper) == b)
        
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            solver.Add(-x[i][j] + P[i - 1][j - 1] >= 0)

    #Minimize Z and Maximize y[i]
    # for i in range(1, M + 1):
    #     solver.Maximize(y[i])
    solver.Minimize(Z)
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print(N)
        for i in range(1, N + 1):
            sys.stdout.write(str(b) + " ") 
            for j in range(1, M + 1):
                if int(x[i][j].solution_value()) == 1: sys.stdout.write(str(j)+" ")
            sys.stdout.write("\n")   
    else:
        sys.stdout.write("No solutions" + "\n") 

    sys.stdout.write(f"Problem solved in {solver.wall_time():d} milliseconds")

if __name__ == "__main__":
    main()
