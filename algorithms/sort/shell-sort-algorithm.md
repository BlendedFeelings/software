---
b: https://blendedfeelings.com/software/algorithms/sort/shell-sort-algorithm.md
---

# ShellSort 
is an in-place comparison-based sorting algorithm that is an extension of insertion sort. The algorithm starts by sorting pairs of elements far apart from each other, then progressively reducing the gap between elements to be compared. By the time the algorithm narrows to comparing adjacent elements, the array has been partially sorted, which improves the performance of insertion sort.

The basic idea of ShellSort is to sort an array by comparing elements that are far apart, then gradually reducing the gap between the elements being compared until the gap is 1. At this point, the algorithm is essentially an insertion sort, but because the array has been partially sorted by the earlier steps, the number of comparisons and swaps required is much smaller than it would be for a standard insertion sort.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/ShellSort.java]
```