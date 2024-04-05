---
b: https://blendedfeelings.com/software/dynamic-programming/memoization.md
---

# Memoization 
is a technique used in dynamic programming to optimize the computation of functions by storing previously calculated results. It is particularly useful when a problem has overlapping subproblems, which means that the same subproblems are solved multiple times. By storing the results of these subproblems, memoization avoids redundant calculations, reducing the time complexity of the algorithm.

Here's how memoization works in the context of dynamic programming:

1. **Identify Overlapping Subproblems**: Determine if the problem can be broken down into smaller subproblems that are solved multiple times.

2. **Create a Storage Structure**: Initialize a data structure (often an array or a hash table) to store the results of the subproblems. This storage is known as the memoization table or cache.

3. **Check for Stored Results**: Before computing a subproblem, check if its result is already stored in the memoization table.

4. **Compute and Store Results**: If the result is not in the table, compute it and then store it in the table for future reference.

5. **Use Stored Results**: When a subproblem needs to be solved again, retrieve the stored result from the memoization table instead of recomputing it.

6. **Return Final Result**: Use the stored results to construct the final solution to the original problem.

Here's a simple example in Python that demonstrates memoization in the context of computing Fibonacci numbers:

```python
def fibonacci(n, memo={}):
    # Check if the result is already in the memoization table
    if n in memo:
        return memo[n]
    
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Compute the result and store it in the memoization table
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    
    # Return the computed result
    return memo[n]

# Example usage
print(fibonacci(10))  # Output: 55
```

In this example, `memo` is a dictionary that stores the computed Fibonacci numbers. Before computing a new Fibonacci number, the function checks if it's already in the `memo`. If it's not, the function computes it recursively and stores the result in `memo`.

Memoization can be applied to many dynamic programming problems, such as calculating the number of ways to climb stairs, finding the longest common subsequence, or solving the 0/1 knapsack problem. It is a powerful technique that can vastly improve the efficiency of algorithms that solve complex problems with overlapping subproblems.