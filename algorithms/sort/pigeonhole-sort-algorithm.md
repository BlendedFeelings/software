---
b: https://blendedfeelings.com/software/algorithms/sort/pigeonhole-sort-algorithm.md
---

# Pigeonhole Sort
is a sorting algorithm that is used to sort elements of an array. It works by determining the range of the input values and creating a set of pigeonholes, or buckets, to hold the values. Each element in the array is then placed in the corresponding pigeonhole, and the values in the pigeonholes are then sorted. The sorted values are then placed back in the original array in order. This algorithm has a time complexity of O(n+k), where n is the number of elements in the array and k is the range of the input values.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/PigeonholeSort.java]
```