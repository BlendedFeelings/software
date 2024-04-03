---
b: https://blendedfeelings.com/software/algorithms/sort/quick-sort-algorithm.md
---

# Quick Sort
is a sorting algorithm that works by selecting a pivot element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively. This process continues until the sub-arrays are small enough to be sorted with a simpler sorting algorithm, such as insertion sort. QuickSort is a widely used sorting algorithm due to its efficiency and average case time complexity of O(n log n).

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/QuickSort.java]
```