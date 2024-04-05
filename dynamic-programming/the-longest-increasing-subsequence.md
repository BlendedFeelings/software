---
b: https://blendedfeelings.com/software/dynamic-programming/the-longest-increasing-subsequence.md
---

# The Longest Increasing Subsequence (LIS) 
is a classic problem in computer science that seeks to find the longest subsequence of a given sequence in which the elements are in sorted order, lowest to highest, and are not necessarily contiguous in the original sequence.

For example, consider the sequence `[10, 22, 9, 33, 21, 50, 41, 60, 80]`. The longest increasing subsequence in this case is `[10, 22, 33, 50, 60, 80]`, which has a length of 6.

There are several ways to solve the LIS problem, including dynamic programming, which is one of the most efficient methods. The dynamic programming approach to finding the LIS has a time complexity of `O(n^2)` for a sequence of length `n`.

### Solution

Here's a simple example of how you might implement the LIS algorithm using dynamic programming in C#:

```csharp
using System;

public class LIS
{
    // Function to find the length of the longest increasing subsequence
    public static int LongestIncreasingSubsequence(int[] arr)
    {
        int n = arr.Length;
        int[] lis = new int[n];

        // Initialize LIS values for all indexes
        for (int i = 0; i < n; i++)
        {
            lis[i] = 1;
        }

        // Compute optimized LIS values in bottom-up manner
        for (int i = 1; i < n; i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (arr[i] > arr[j] && lis[i] < lis[j] + 1)
                {
                    lis[i] = lis[j] + 1;
                }
            }
        }

        // Pick maximum of all LIS values
        int max = 0;
        for (int i = 0; i < n; i++)
        {
            if (max < lis[i])
            {
                max = lis[i];
            }
        }

        return max;
    }

    // Main method to test the function
    public static void Main()
    {
        int[] arr = { 10, 22, 9, 33, 21, 50, 41, 60, 80 };
        int result = LongestIncreasingSubsequence(arr);
        Console.WriteLine("Length of LIS is " + result);
    }
}
```

This code defines a function `LongestIncreasingSubsequence` which takes an array of integers as input and returns the length of the LIS. The `Main` method is used to test this function with a sample array.

Please note that this implementation only finds the length of the LIS, not the subsequence itself. To reconstruct the actual LIS, you would need to modify the algorithm to track the sequence as well as the lengths.