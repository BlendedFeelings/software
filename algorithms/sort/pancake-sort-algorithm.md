---
b: https://blendedfeelings.com/software/algorithms/sort/pancake-sort-algorithm.md
---

# Pancake Sort
is a sorting algorithm that sorts an array by repeatedly flipping the order of its elements. It works by finding the largest element in the unsorted part of the array and flipping the sub-array from the first element to the largest element, so that the largest element is now at the beginning of the array. Then, it flips the entire array, so that the largest element is now at the end of the array. This process is repeated for the remaining unsorted part of the array until the entire array is sorted. The time complexity of Pancake sort is O(n^2), where n is the number of elements in the array.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/PancakeSort.java]
```