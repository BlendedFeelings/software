---
b: https://blendedfeelings.com/software/algorithms/searche/ternary-search-algorithm.md
---

# Ternary search
is a divide and conquer algorithm used to search an element in a sorted array. It is similar to binary search, but instead of dividing the array into two parts, it divides it into three parts.

The algorithm works by first dividing the array into three parts, and determining which part of the array the element is in. If the element is in the first part, the algorithm recursively searches the first part. If it is in the second part, the algorithm recursively searches the second part. If it is in the third part, the algorithm recursively searches the third part.

The time complexity of ternary search is O(log3 n), which is slightly better than binary search's time complexity of O(log2 n) in the worst case. However, the constant factors involved in ternary search are larger than binary search, so in practice, binary search is often faster.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/searches/TernarySearch.java]
```