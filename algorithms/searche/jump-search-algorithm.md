---
b: https://blendedfeelings.com/software/algorithms/searche/jump-search-algorithm.md
---

# Jump Search (also known as Block Search) 
is a searching algorithm for sorted arrays. It works by jumping ahead by fixed steps or blocks in the array, instead of traversing the entire array. Once the block containing the target element is found, a linear search is performed within that block to find the exact location of the element.

The time complexity of Jump Search is O(√n), which is better than linear search but worse than binary search. It is useful for large arrays where binary search is not efficient due to high overheads, and where the array elements are uniformly distributed.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/searches/JumpSearch.java]
```