---
b: https://blendedfeelings.com/software/dynamic-programming/the-coin-change-problem.md
---

# The Coin Change Problem 
is a classic algorithmic challenge that involves finding the number of ways to make change for a particular amount of money given a set of coin denominations. It is a variation of the unbounded knapsack problem and is commonly solved using dynamic programming.

Here's the problem statement:

Given an amount \( N \) and a set of coin denominations \( D = \{d_1, d_2, \ldots, d_m\} \), find the number of ways to make change for \( N \) using any number of coins from the set \( D \).

For example, if you have to make change for 4 units of currency and you have coin denominations of 1, 2, and 3 units, there are four ways to make change:

1. \( 1 + 1 + 1 + 1 \)
2. \( 1 + 1 + 2 \)
3. \( 2 + 2 \)
4. \( 1 + 3 \)


### Solution
Here is a Python function that uses dynamic programming to solve the Coin Change Problem:

```python
def coin_change(coins, amount):
    # Create an array to store the solutions to the subproblems
    dp = [0] * (amount + 1)
    
    # Base case: There is one way to make 0, which is to use no coins
    dp[0] = 1
    
    # Solve for all amounts from 1 to the target amount
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    
    # The answer is stored in dp[amount]
    return dp[amount]

# Example usage:
coins = [1, 2, 5]  # The denominations of the coins
amount = 11  # The target amount
print(coin_change(coins, amount))  # Output the number of ways to make the amount
```

To explain the dynamic programming approach used in this function:

1. We initialize a list `dp` with a length of `amount + 1` to store the number of ways to make each value from 0 up to the target amount. We initialize `dp[0]` to 1 because there is exactly one way to make the amount 0, which is to use no coins.

2. We then iterate over each coin denomination and update the `dp` array. For each coin, we iterate through all the amounts from the coin's value up to the target amount. For each amount `x`, we add the value of `dp[x - coin]` to `dp[x]`. This represents the idea that the number of ways to make amount `x` includes the number of ways to make `x - coin` (since we can add the current coin to those combinations).

3. After we've processed all the coins, the value at `dp[amount]` will be the total number of distinct ways to make up the amount using the given denominations.

Please note that this function gives the number of ways to make change, not the actual combinations of coins. If you need to track the combinations themselves, the problem becomes more complex and requires a different approach.