---
b: https://blendedfeelings.com/software/algorithms/sort/radix-sort-algorithm.md
---

# Radix Sort
is a non-comparative sorting algorithm that sorts data with integer keys by grouping the keys by individual digits that share the same significant position and value (place value). It is a linear time complexity sorting algorithm that has a time complexity of O(d(n+k)), where d is the number of digits in the maximum number, n is the number of elements to be sorted, and k is the range of the input. Radix sort can be used for sorting numbers, strings, and other data types that can be converted to integers.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/RadixSort.java]
```