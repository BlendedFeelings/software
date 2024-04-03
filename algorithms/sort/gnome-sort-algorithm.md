---
b: https://blendedfeelings.com/software/algorithms/sort/gnome-sort-algorithm.md
---

# Gnome Sort
is a sorting algorithm that works by moving elements one position to the left or right, until the element is in the correct position. It is similar to Insertion Sort, but instead of comparing adjacent elements, it compares the current element with the element in the previous position. If the current element is smaller than the previous element, it swaps the two elements and moves one position to the left. If the current element is larger than the previous element, it moves one position to the right. This process is repeated until the entire array is sorted. The time complexity of GnomeSort is O(n^2), which makes it less efficient than other sorting algorithms like MergeSort or QuickSort.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/GnomeSort.java]
```