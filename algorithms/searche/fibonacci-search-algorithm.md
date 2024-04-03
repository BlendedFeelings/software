---
b: https://blendedfeelings.com/software/algorithms/searche/fibonacci-search-algorithm.md
---

# Fibonacci search
is a searching algorithm that is a variant of binary search algorithm. It is used to search for an element in a sorted array by dividing the array into two parts that have sizes in the ratio of two consecutive Fibonacci numbers. The algorithm uses Fibonacci numbers to determine the split position and compares the key with the middle element. If the key is smaller, it searches in the first subarray, otherwise it searches in the second subarray. This process is repeated until the key is found or the subarray size becomes 1.

Fibonacci search has a time complexity of O(log n) and is generally faster than binary search, especially for large arrays. However, it requires that the array be sorted and the computation of Fibonacci numbers can be expensive.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/searches/FibonacciSearch.java]
```