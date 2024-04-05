---
b: https://blendedfeelings.com/software/dynamic-programming/the-knapsack-problem.md
---

# The Knapsack Problem 
is a classic problem in combinatorial optimization.
You are a thief carrying a knapsack that can hold a certain weight, and there are various items that you can steal. Each item has a weight and a value. The goal is to maximize the total value of the items you steal without exceeding the weight capacity of the knapsack.

There are several variations of the Knapsack Problem, but the most common one is the 0/1 Knapsack Problem, where each item can be taken or left (i.e., you cannot take a fractional part of an item). The problem is called "0/1" because the solution is in binary terms—either 0 (do not take the item) or 1 (take the item).

The mathematical formulation of the 0/1 Knapsack Problem is as follows:

Given:
- A set of $n$ items, each with a weight $w_i$ and a value $v_i$.
- A knapsack with a weight capacity $W$.

Find:
- A vector $x = (x_1, x_2, ..., x_n)$ where $x_i$ is either 0 or 1, representing whether item $i$ is taken or not.

Objective:
- Maximize $\sum_{i=1}^{n} v_i x_i$ (the total value of the knapsack).

Subject to:
- $\sum_{i=1}^{n} w_i x_i \leq W$ (the total weight of the knapsack does not exceed its capacity).

The problem is NP-complete, which means that there is no known polynomial-time algorithm to solve it for all instances. However, there are several approaches to find an optimal or near-optimal solution, such as dynamic programming, greedy algorithms (which do not always yield an optimal solution), and various heuristic or approximation algorithms.

### Solution
Here is a Python function that solves the 0/1 Knapsack problem using dynamic programming. In the 0/1 Knapsack problem, you can either take an entire item or leave it (no fractional items allowed).

```python
def knapSack(W, wt, val, n):
    """
    Solve the knapsack problem by finding the most valuable subsequence of `val`
    subject to the weight constraint `W`.

    Parameters:
    W : int
        Maximum weight capacity of the knapsack
    wt : list of int
        Weights of the items
    val : list of int
        Values (profits) of the items
    n : int
        Number of items

    Returns:
    int
        The maximum value that fits in the knapsack of capacity W
    """
    # Create a 2D array `dp` where dp[i][w] represents the maximum value that can
    # be attained with the first `i` items and a weight limit of `w`.
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build the dp array from bottom up
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            # If the weight of the current item is greater than the current weight
            # capacity `w`, we can't include this item in the current subset
            if wt[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Otherwise, we consider two cases:
                # 1. Including the current item and adding its value to the maximum value
                #    of the remaining weight capacity `w - wt[i-1]`
                # 2. Excluding the current item and taking the maximum value of the same
                #    weight capacity without considering this item
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i-1]] + val[i-1])

    # The last cell of the dp array contains the answer
    return dp[n][W]

# Example usage:
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))
```

In this example, `W` is the maximum weight your knapsack can carry, `wt` is a list of the weights of each item, `val` is a list of the values of each item, and `n` is the number of items. The function returns the maximum value that can fit in the knapsack.

Remember that this implementation does not return the items that make up the optimal solution, only the total value of the optimal solution. To reconstruct which items are included in the optimal solution, you would need to trace back through the `dp` array.