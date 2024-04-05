---
b: https://blendedfeelings.com/software/dynamic-programming/the-matrix-chain-multiplication-problem.md
---

# The Matrix Chain Multiplication (MCM) problem 
is a classic optimization problem that falls under the category of dynamic programming. The problem involves finding the most efficient way to multiply a given sequence of matrices.

Given a chain of matrices \( A_1, A_2, \ldots, A_n \), where each matrix \( A_i \) has dimensions \( p_{i-1} \times p_i \), the goal is to determine the order of multiplications that minimizes the total number of scalar multiplications needed to compute the product \( A_1 \times A_2 \times \ldots \times A_n \).

The problem arises because matrix multiplication is associative, meaning that no matter how the products are grouped, the result will be the same. However, the number of operations required can vary greatly depending on the order in which the matrices are multiplied.

For example, consider three matrices \( A \), \( B \), and \( C \) with dimensions \( 10 \times 30 \), \( 30 \times 5 \), and \( 5 \times 60 \), respectively. Multiplying them as \( (AB)C \) requires \( 10 \times 30 \times 5 + 10 \times 5 \times 60 = 4500 \) scalar multiplications, while multiplying them as \( A(BC) \) requires \( 30 \times 5 \times 60 + 10 \times 30 \times 60 = 27000 \) scalar multiplications. Clearly, the first option is more efficient.

The MCM problem can be solved using dynamic programming by constructing a table \( m \) where \( m[i, j] \) represents the minimum number of scalar multiplications needed to compute the matrix \( A_i \times A_{i+1} \times \ldots \times A_j \). The solution involves filling in this table using a bottom-up approach.

### Solution
Here's the Python version of the Matrix Chain Multiplication algorithm, which uses dynamic programming to solve the problem:

```python
def matrix_chain_order(p):
    n = len(p) - 1
    # m[i][j] is the minimum number of multiplications needed
    # to compute the matrix A[i]A[i+1]...A[j] = A[i..j]
    # cost is zero when multiplying one matrix
    m = [[0 for x in range(n)] for x in range(n)]

    # s[i][j] is the index of the matrix after which the product is split
    # in an optimal parenthesization of the matrix A[i]A[i+1]...A[j] = A[i..j]
    s = [[0 for x in range(n)] for x in range(n)]

    # L is the chain length
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                # q = cost/scalar multiplications
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i + 1}", end='')
    else:
        print("(", end='')
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end='')

# Example usage:
p = [30, 35, 15, 5, 10, 20, 25]  # Dimensions of the matrices
m, s = matrix_chain_order(p)
print("Minimum number of multiplications is:", m[0][len(p) - 2])
print("Optimal parenthesization is:", end=' ')
print_optimal_parens(s, 0, len(p) - 2)
```

This Python code defines two functions: `matrix_chain_order` and `print_optimal_parens`. The `matrix_chain_order` function calculates the minimum number of scalar multiplications needed to multiply the chain of matrices, and `print_optimal_parens` prints the optimal parenthesization of the matrix multiplication.

The `p` array contains the dimensions of the matrices such that the `i`-th matrix has dimensions `p[i-1] x p[i]`. The example usage at the end of the script demonstrates how to use these functions with a given sequence of matrix dimensions.