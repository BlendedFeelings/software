---
b: https://blendedfeelings.com/software/algorithms/searche/recursive-binary-search-algorithm.md
---

# Recursive Binary Search 
is a searching algorithm that uses the divide and conquer strategy to search for an element in a sorted array. The algorithm compares the target element with the middle element of the array. If they are equal, the search is complete. If the target is less than the middle element, the algorithm searches in the left half of the array. If the target is greater than the middle element, the algorithm searches in the right half of the array. This process is repeated recursively until the target element is found or the array is exhausted.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/searches/RecursiveBinarySearch.java]
```