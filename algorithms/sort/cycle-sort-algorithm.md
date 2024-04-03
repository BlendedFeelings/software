---
b: https://blendedfeelings.com/software/algorithms/sort/cycle-sort-algorithm.md
---

# Cycle Sort
is unstable sorting algorithm that is optimal for situations where the write time to memory is significantly more expensive than the time to perform comparisons. It works by dividing the array into cycles, where each cycle contains elements that belong to the same position in the final sorted array. The algorithm then iterates through each cycle, swapping elements until the element in the current cycle is in its correct position. This process is repeated until all elements are in their correct position. Cycle sort has a time complexity of O(n^2), but it is often faster than other O(n^2) algorithms, such as bubble sort and selection sort, due to its reduced number of writes to memory.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/CycleSort.java]
```