---
b: https://blendedfeelings.com/software/dynamic-programming/tabulation.md
---

# Tabulation 
is a bottom-up approach to dynamic programming. It involves solving smaller subproblems first and using their solutions to build up solutions to larger subproblems. This approach is iterative and typically uses an array (or a table) to store the results of subproblems. The main idea is to fill up the table in a way that each entry of the array/table is solved only once and stored for future reference, thus avoiding the need for redundant calculations.

Here's a step-by-step guide to using tabulation in dynamic programming:

1. **Identify the subproblems**: Break down the main problem into smaller subproblems that can be solved independently.

2. **Create the table**: Initialize an array or a matrix to store the solutions to the subproblems. The dimensions of the table will depend on the number of variables upon which the subproblems depend.

3. **Base cases**: Fill in the base cases in the table. These are the smallest subproblems that can be solved without depending on other subproblems.

4. **Iterative solution**: Fill in the rest of the table in a systematic way. This often involves iterating over the dimensions of the table and solving for each entry based on previously filled entries.

5. **Transition function**: Define a transition function that describes how to compute the value of a subproblem based on the values of its dependencies (earlier solved subproblems).

6. **Return the final solution**: After filling the table, the final solution to the original problem will typically be found in a specific cell of the table (e.g., the last cell).

Here's the equivalent Python code for the pseudocode example of the tabulated Fibonacci sequence:

```python
def tabulated_fibonacci(n):
    if n <= 1:
        return n

    # Step 2: Create the table with n+1 entries
    fib = [0] * (n + 1)

    # Step 3: Base cases
    fib[0] = 0
    fib[1] = 1

    # Step 4: Iterative solution
    for i in range(2, n + 1):
        # Step 5: Transition function
        fib[i] = fib[i - 1] + fib[i - 2]

    # Step 6: Return the final solution
    return fib[n]

# Example usage:
print(tabulated_fibonacci(10))  # Output: 55
```

In this Python function, `fib` is a list that serves as the table to store Fibonacci numbers. The base cases `fib[0]` and `fib[1]` are set to `0` and `1`, respectively. The `for` loop fills in the rest of the list using the transition function, which is the sum of the two previous Fibonacci numbers. Finally, the function returns the `n`th Fibonacci number from the list.

Tabulation is particularly useful when the order of solving subproblems is straightforward and doesn't involve recursion, making it more memory-efficient and often faster than the top-down memoization approach.