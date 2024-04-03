---
b: https://blendedfeelings.com/software/algorithms/sort/dual-pivot-quicksort-algorithm.md
---

# Dual-Pivot Quicksort
is a sorting algorithm that is an improvement over the traditional Quicksort algorithm. It was introduced by Vladimir Yaroslavskiy in 2009 and is used in Java's Arrays.sort() method.

The algorithm works by selecting two pivots instead of one and partitioning the array into three parts: elements less than the first pivot, elements between the first and second pivot, and elements greater than the second pivot. The algorithm then recursively sorts the left and right partitions using the same process until the entire array is sorted.

Dual-Pivot Quicksort has been shown to be faster than traditional Quicksort on average and has better worst-case performance. It also has the advantage of being stable, meaning that the order of equal elements is preserved.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/DualPivotQuickSort.java]
```