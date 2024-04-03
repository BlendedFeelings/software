---
b: https://blendedfeelings.com/software/algorithms/sort/comb-sort-algorithm.md
---

# Comb Sort
is a comparison-based sorting algorithm and is an improvement over the bubble sort algorithm. Comb sort works by comparing and swapping adjacent elements that are separated by a gap. The gap starts as the length of the array being sorted and is divided by a shrink factor (usually 1.3) until it reaches a minimum value of 1. This helps to eliminate the "turtles" (small values near the end of the list) that slow down the bubble sort algorithm. Comb sort has an average-case time complexity of O(n log n), making it faster than bubble sort for large data sets.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/CombSort.java]
```