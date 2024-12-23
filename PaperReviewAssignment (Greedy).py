import sys
import time


[N, M, b] = [int(x) for x in sys.stdin.readline().split()]
lst = dict()
L = []
for i in range(N):
    lst[i + 1] = [int(x) for x in sys.stdin.readline().split()]
    L.append(lst[i + 1][1:])

load = [[0, i] for i in range(M + 1)]

assignments = []

start = time.time()
for i in range(N):
    tmp = 0
    load.sort()
    assignment = []
    for t in load:
        if t[1] in L[i]:
            assignment.append(t[1])
            tmp += 1
            t[0] += 1
        if tmp == b:
            break            
    assignments.append(assignment)

end = time.time()

print(N)
for assignment in assignments:
    print(b, end = ' ')
    print(*assignment)

print(end - start)
