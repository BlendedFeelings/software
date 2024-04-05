---
b: https://blendedfeelings.com/software/dynamic-programming/optimal-substructure.md
---

# Optimal substructure 
is a key property that a problem must have in order for dynamic programming (DP) to be applicable. This property means that an optimal solution to the problem can be constructed efficiently from optimal solutions to its subproblems.

Here's what optimal substructure implies in the context of dynamic programming:

1. **Overlapping Subproblems**: The problem can be broken down into smaller, simpler subproblems which are solved independently.
2. **Optimal Substructure**: The optimal solution to the problem contains within it optimal solutions to the subproblems.

For a problem to have optimal substructure, it must be the case that if you take the optimal solution for a larger problem, and consider the choices made to reach that solution, each of those choices must have been optimal for the subproblem that it solved.

In simpler terms, it means that the best way to solve the whole problem can be found by combining the best solutions to its smaller parts. Here's a breakdown:

- **Breaking Down Problems**: Imagine you have a big problem. You can chop it up into smaller pieces that are easier to manage. These pieces are called subproblems.

- **Solving the Little Pieces**: You figure out the best solution for each of these small subproblems. These solutions are optimal, meaning they're the best you can get for each piece.

- **Building Up Solutions**: Once you have the best solutions for all the small pieces, you can put them together like a puzzle to solve the big problem. The key point is that the best solution for the big problem is made up of the best solutions for the smaller problems.


For instance, in the shortest path problem, if the shortest path from point A to point C goes through point B, then the path from A to B must be the shortest path between those two points. If it were not, then we could find a shorter path from A to C by first going to B along this shorter path, which would contradict our assumption that we had found the shortest path from A to C.

Dynamic programming solutions typically follow a pattern where they solve all subproblems of a smaller size before attempting to solve larger ones (bottom-up approach), or they start with the larger problem and recursively solve the subproblems as they are encountered (top-down approach with memoization). The optimal substructure property ensures that by combining the solutions to the subproblems in this way, we are guaranteed to arrive at the overall optimal solution.

It's important to note that not all problems have an optimal substructure, which makes them unsuitable for dynamic programming solutions. Identifying the optimal substructure is often one of the first steps in designing a dynamic programming algorithm.