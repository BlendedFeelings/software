---
b: https://blendedfeelings.com/software/algorithms/sort/heap-sort-algorithm.md
---

# Heap Sort
is a comparison-based sorting algorithm that works by building a binary heap from the input array and then repeatedly extracting the maximum element and placing it at the end of the sorted array. The heap is a complete binary tree that satisfies the heap property, which states that the parent node must be greater than or equal to its children. By repeatedly extracting the maximum element, the array is sorted in descending order. The time complexity of HeapSort is O(n log n) in the worst case, where n is the number of elements in the array.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/HeapSort.java]
```