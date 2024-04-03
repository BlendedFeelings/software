---
b: https://blendedfeelings.com/software/algorithms/sort/selection-sort-algorithm.md
---

# Selection Sort 
is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of an array and putting it at the beginning of the array.

The algorithm maintains two subarrays in a given array:
1. The subarray which is already sorted.
2. Remaining subarray which is unsorted.

The algorithm iterates through the unsorted subarray, finds the smallest element and swaps it with the leftmost unsorted element. This process continues until the entire array is sorted.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/SelectionSort.java]
```