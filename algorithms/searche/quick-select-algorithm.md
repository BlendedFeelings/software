---
b: https://blendedfeelings.com/software/algorithms/searche/quick-select-algorithm.md
---

# QuickSelect
is a selection algorithm used to find the k-th smallest element in an unsorted list or array. It is a variation of the QuickSort algorithm, which is a sorting algorithm. The QuickSelect algorithm works by selecting a pivot element from the list and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The algorithm then recursively processes the sub-array that contains the k-th smallest element until it is found.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/searches/QuickSelect.java]
```