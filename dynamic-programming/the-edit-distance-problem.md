---
b: https://blendedfeelings.com/software/dynamic-programming/the-edit-distance-problem.md
---

# The Edit Distance problem
also known as the Levenshtein distance, is a measure of the similarity between two strings. It is defined as the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into the other. This metric is useful in various applications, such as spell checking, DNA sequencing, and natural language processing.

### Solution

To solve the Edit Distance problem using dynamic programming, you can implement the algorithm in a programming language of your choice. Below is an example implementation in Python, which is commonly used for its readability and ease of use in algorithmic challenges:

```python
def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Create a matrix to store the distances
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    
    # Initialize the matrix
    for i in range(m+1):
        for j in range(n+1):
            # If first string is empty, all characters of second string need to be inserted
            if i == 0:
                dp[i][j] = j
            # If second string is empty, all characters of first string need to be removed
            elif j == 0:
                dp[i][j] = i
            # If last characters are the same, ignore the last character and continue
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # If the last character is different, consider all possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # Remove
                                   dp[i][j-1],    # Insert
                                   dp[i-1][j-1])  # Replace
    
    # The value in the bottom right corner of the matrix is the edit distance
    return dp[m][n]

# Example usage:
str1 = "kitten"
str2 = "sitting"
print(edit_distance(str1, str2))  # Output: 3
```

This Python function `edit_distance` takes two strings `str1` and `str2` as input and returns the edit distance between them. The matrix `dp` is initialized with size `(m+1) x (n+1)` where `m` and `n` are the lengths of the two strings. The matrix is then filled out according to the rules of the algorithm, and the final value in `dp[m][n]` is returned, representing the minimum number of edits required to transform `str1` into `str2`.

The time complexity of this algorithm is `O(m*n)` because it fills out an `m x n` matrix with constant-time operations. The space complexity is also `O(m*n)` due to the storage requirements of the matrix.