# Fundamental-of-Optimization-Mini-Project
Topic 14 - Paper Reviewer Assignment

The chair of a conference must assign scientific papers to reviewers in a balance way. There are N papers 1, 2, …, N and M reviewers 1, 2, …, M. Each paper i has a list L(i) of reviewers who are willing to review that paper. A review plan is an assignment reviewers to papers. The load of a reviewer is the number of papers he/she have to review. Given a constant b, compute the assignment such that:
- Each paper is reviewed by exactly b reviewers
- The maximum load of all reviewers is minimal
- In the solution, each paper i is represented by a list r(i, 1), r(i, 2), . . ., r(i, b) of b reviewers asssigned to this paper

Input:
  Line 1 contains N, M and b
  Line i+1 (i = 1,…,N) contains a positive integer k followed by k positive integers representing the list L(i)
Output:
 Line 1: contains N
 Line i + 1 (i = 1, . . ., N): contains b and b integers r(i, 1), r(i, 2), . . ., r(i, b) which are the list of reivewers assigned to paper i

Example:

Input:
    5 3 2
    3 1 2 3 
    2 1 2
    3 1 2 3
    3 1 2 3 
    2 1 3

Output:
    5
    2 1 2
    2 1 2
    2 3 1
    2 3 2
    2 3 1
