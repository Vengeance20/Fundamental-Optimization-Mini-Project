from itertools import combinations

# Input function to parse data
def read_input():
    """
    Read input for the problem. Parse the number of papers (n), reviewers (m),
    and number of reviewers needed per paper (b). Also parse the list of preferences
    for each paper.
    """
    n, m, b = map(int, input().split())  # Number of papers, reviewers, and b
    paper_preferences = []
    for _ in range(n):
        line = list(map(int, input().split()))
        paper_preferences.append(line[1:])  # Ignore the first number (k)
    return n, m, b, paper_preferences

# Backtracking function to find the optimal assignment
def find_optimal_assignment(n, m, b, paper_preferences):
    """
    Use backtracking to find the optimal assignment of reviewers to papers,
    minimizing the maximum workload of any reviewer.
    """
    # Initialize variables
    min_load = float('inf')  # Minimum maximum load found so far
    best_assignment = None  # Store the best assignment found
    load = [0] * (m + 1)  # Track the workload of each reviewer
    current_assignment = [None] * n  # Current assignment for papers

    # Define the backtracking function
    def backtrack(paper):
        nonlocal min_load, best_assignment

        # Base case: All papers have been assigned
        if paper == n:
            max_load = max(load)  # Calculate the maximum workload
            if max_load < min_load:  # Update the best solution if found
                min_load = max_load
                best_assignment = [list(assignment) for assignment in current_assignment]
            return

        # Sort preferences of reviewers for the current paper based on their current load (lighter reviewers first)
        sorted_reviewers = sorted(paper_preferences[paper], key=lambda r: load[r])

        # Check if there are enough reviewers available 
        if len(sorted_reviewers) < b:
            print("No available assignment")
            exit()  # Stop if there are not enough reviewers for this paper

        else:
        # Proceed with normal pruning if it's not the case
            # Try all combinations of b reviewers for the current paper
            for reviewers in combinations(sorted_reviewers, b):
                # Check and update load
                valid = True
                updated_reviewers = []   # List to store reviewers whose load has been increased
                for reviewer in reviewers:
                    updated_reviewers.append(reviewer)  # Record the reviewer whose load was increased
                    load[reviewer] += 1     # Temporarily increase workload for the selected reviewers
                    if load[reviewer] > min_load:  # Prune if load exceeds current minimum
                        valid = False
                        break

                if valid:  # Proceed only if valid
                    current_assignment[paper] = reviewers
                    backtrack(paper + 1)

                # Revert load (backtrack step) only for reviewers in updated_reviewers
                for reviewer in updated_reviewers:
                    load[reviewer] -= 1

    # Start backtracking from the first paper
    backtrack(0)
    return best_assignment

# Main function
def main():
    """
    Main function to handle input, process the problem, and output the result.
    """
    # Step 1: Read input
    n, m, b, paper_preferences = read_input()

    # Step 2: Find the optimal assignment
    optimal_assignment = find_optimal_assignment(n, m, b, paper_preferences)

    # Print the number of papers and their assignments
    print(n)
    for paper in range(n):
        print(b, *optimal_assignment[paper])

# Run the program
if __name__ == "__main__":
    main()