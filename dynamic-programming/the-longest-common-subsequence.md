---
b: https://blendedfeelings.com/software/dynamic-programming/the-longest-common-subsequence.md
---

# The Longest Common Subsequence (LCS) problem 
is a classic computer science problem that is used to find the longest subsequence common to all sequences in a set of sequences (often just two). A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. LCS is a well-studied problem in the field of dynamic programming and has applications in various areas such as bioinformatics, text comparison, and version control.

The problem can be formally defined as follows:

Given two sequences, find the length of the longest subsequence present in both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, "abc", "abg", "bdf", "aeg", "acefg", etc. are subsequences of "abcdefg".

For example, consider the following two sequences:

```
X: ABCBDAB
Y: BDCABC
```

The length of the LCS is `4` and the LCS is `BCAB` or `BDAB`.

### Solution

To solve the Longest Common Subsequence (LCS) problem using dynamic programming, we create a 2D table that stores the lengths of the longest common subsequences for different parts of the two input sequences. Below is a Python example that demonstrates how to implement the LCS algorithm using dynamic programming:

```python
def lcs(X, Y):
    # Find the length of the strings
    m = len(X)
    n = len(Y)
  
    # Create a 2D table to store lengths of LCS of substrings. Note that we use
    # (m+1) x (n+1) table as we also need to consider the empty string (0 length)
    # as a part of our subproblems.
    L = [[0] * (n+1) for i in range(m+1)]
  
    # Build the table in bottom-up fashion
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
  
    # Following code is used to print LCS
    index = L[m][n]
  
    # Create a string variable to store the LCS string
    lcs = [""] * (index+1)
    lcs[index] = ""
  
    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:
  
        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
  
        # If not same, then find the larger of two and
        # go in the direction of the larger value
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
  
    # The lcs string is now constructed in reverse order.
    # Join the array to get the final LCS string
    lcs_str = "".join(lcs)
    return lcs_str

# Example usage:
X = "ABCBDAB"
Y = "BDCABC"
print("LCS of " + X + " and " + Y + " is " + lcs(X, Y))
```

This code defines a function `lcs` that takes two strings `X` and `Y` as input and returns the longest common subsequence. The function constructs the 2D table `L` that records the lengths of LCSs for all combinations of subproblems. It then constructs the actual LCS string by tracing back from `L[m][n]`.

The time complexity of this algorithm is `O(m*n)`, where `m` is the length of string `X` and `n` is the length of string `Y`. The space complexity is also `O(m*n)` due to the 2D table used for storing the lengths.