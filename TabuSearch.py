from collections import defaultdict
import heapq

def assign_reviewers(N, M, b, paper_reviewer_lists):
    # Reviewer loads
    reviewer_loads = [0] * (M + 1)  # Index 1-based for reviewers
    assignments = []  # To store results
    
    # Priority queue for reviewer loads (min-heap)
    min_heap = [(0, i) for i in range(1, M + 1)]
    heapq.heapify(min_heap)
    
    for i in range(N):
        k, *reviewer_list = paper_reviewer_lists[i]
        possible_reviewers = set(reviewer_list)
        
        # Select b reviewers with the least load
        selected_reviewers = []
        temp_heap = []
        
        while len(selected_reviewers) < b:
            load, reviewer = heapq.heappop(min_heap)
            if reviewer in possible_reviewers:
                selected_reviewers.append(reviewer)
                reviewer_loads[reviewer] += 1
                heapq.heappush(temp_heap, (reviewer_loads[reviewer], reviewer))
            else:
                heapq.heappush(temp_heap, (load, reviewer))
        
        # Push remaining back into the heap
        while min_heap:
            temp_heap.append(heapq.heappop(min_heap))
        
        heapq.heapify(temp_heap)
        min_heap = temp_heap
        assignments.append(selected_reviewers)
    
    return assignments

# Input
N, M, b = map(int, input().split())
paper_reviewer_lists = [list(map(int, input().split())) for _ in range(N)]

# Assign reviewers
assignments = assign_reviewers(N, M, b, paper_reviewer_lists)

# Output
print(N)
for a in assignments:
    print(b, *a)