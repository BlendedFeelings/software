---
b: https://blendedfeelings.com/software/dynamic-programming/dynamic-programming.md
---

# Dynamic programming (DP) 
is a method for solving complex problems by breaking them down into simpler subproblems. It is applicable to problems that exhibit the properties of overlapping subproblems and optimal substructure. Dynamic programming is mainly used when the calculations of the subproblems are needed repeatedly in the process of finding the solution to the bigger problem.

Here are the key concepts of dynamic programming:

1. **Overlapping Subproblems**: The problem can be broken down into subproblems which are reused several times.

2. **Optimal Substructure**: The optimal solution to the problem can be constructed from optimal solutions to its subproblems.

3. **Memoization**: This technique involves storing the solutions to subproblems in a table (usually an array) so that these don't have to be recomputed, which saves time at the expense of memory.

4. **Tabulation**: This is a bottom-up approach where you solve all the subproblems first, typically by filling up an n-dimensional table based on the number of parameters that affect the outcome, and use the stored solutions to solve bigger and bigger problems.

5. **State**: A state represents a subproblem. It usually corresponds to a set of variables that captures all the necessary information to process a particular instance of the problem.

6. **Transition**: A rule or function that describes how to move from one state to another.

A classic example of a problem where dynamic programming is used is the Fibonacci sequence, where each number is the sum of the two preceding ones. Without DP, you would calculate the same Fibonacci numbers many times if you use a simple recursive approach. With memoization or tabulation, you calculate each Fibonacci number only once, saving on unnecessary computations.

Other common problems that can be solved using dynamic programming include:

- The Knapsack Problem
- The Coin Change Problem
- The Longest Common Subsequence
- The Longest Increasing Subsequence
- The Edit Distance Problem
- The Matrix Chain Multiplication Problem

To implement a dynamic programming solution, one typically follows these steps:

1. Define the structure of the optimal solution.
2. Recursively define the value of the optimal solution.
3. Compute the value of the optimal solution (typically in a bottom-up fashion).
4. Construct an optimal solution from the computed information.

Dynamic programming can be quite challenging to grasp and apply correctly, but it's a powerful tool in the arsenal of algorithmic problem-solving techniques.