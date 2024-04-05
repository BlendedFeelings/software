---
b: https://blendedfeelings.com/software/dynamic-programming/overlapping-subproblem.md
---

# Overlapping subproblems 
is a property of a computational problem that indicates the problem can be broken down into subproblems which are reused several times. This property is one of the main characteristics that make a problem suitable for dynamic programming, a method for efficiently solving complex problems by breaking them down into simpler subproblems.

In simple terms, "overlapping subproblems" refers to a situation in a computational problem where the same smaller problems occur over and over again within the process of solving a larger problem. Instead of solving these smaller problems repeatedly, we can solve each unique small problem once and store the solution. Then, whenever we encounter the same problem again, we can simply reuse the already computed solution.

In the context of dynamic programming, there are generally two key attributes that a problem must have to be effectively solved using this approach:

1. **Optimal Substructure**: The solution to the problem can be composed of optimal solutions to its subproblems.
2. **Overlapping Subproblems**: The problem can be broken down into subproblems which are not independent, i.e., the subproblems recur multiple times.

### Types of Overlapping Subproblems:

- **Memoization**: This is a top-down approach where you solve the problem by first breaking it down into subproblems and then solving those subproblems. Importantly, each time you solve a subproblem, you store its result in some sort of data structure (e.g., an array or a hash table). If the same subproblem appears again, you simply look up the previously computed result, rather than recomputing it. This saves computation time at the expense of some additional space for the memoization table.
  
- **Tabulation**: This is a bottom-up approach where you first understand how to solve the smallest subproblems (those that do not depend on any other subproblems), and then solve larger and larger subproblems until you solve the original problem. With tabulation, you typically fill up a table (hence the name) based on the results of smaller subproblems. Since you fill the table iteratively, you are guaranteed to have solved all the necessary smaller subproblems before tackling a larger subproblem.

### Examples of Problems with Overlapping Subproblems:

- **Fibonacci Numbers**: The Fibonacci sequence is a classic example of a problem with overlapping subproblems. The nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers. When you use a naive recursive approach to compute the nth Fibonacci number, you end up computing the same subproblems multiple times. Dynamic programming approaches like memoization or tabulation can significantly reduce the number of computations.

- **Shortest Path Problems**: In graph theory, problems like finding the shortest path from a starting node to a destination node can have overlapping subproblems, especially in weighted graphs where you might revisit nodes multiple times to find the shortest path.

- **Knapsack Problem**: The 0/1 knapsack problem, where you have to maximize the total value of items you can carry in a knapsack of limited capacity, also exhibits overlapping subproblems. When you break down the problem, you find that the same subproblems (with particular items and capacities) are solved repeatedly.

When a problem has overlapping subproblems, dynamic programming can be a very effective strategy to optimize the solution process. It avoids redundant computations and thus can greatly improve the efficiency of the solution in terms of time complexity.