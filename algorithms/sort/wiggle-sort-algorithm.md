---
b: https://blendedfeelings.com/software/algorithms/sort/wiggle-sort-algorithm.md
---

# WiggleSort
is an algorithm that rearranges an array of integers in a specific way. The goal is to make the array "wiggle" by arranging the elements in a sequence such that:

- The first element is less than or equal to the second element
- The second element is greater than or equal to the third element
- The third element is less than or equal to the fourth element
- And so on...

In other words, the array should alternate between peaks and valleys. For example, if the original array is [3, 5, 2, 1, 6, 4], the WiggleSort algorithm would rearrange it to [3, 5, 1, 6, 2, 4].

The algorithm works by iterating through the array and swapping adjacent elements if they are not in the correct order. If the current index is even, it checks if the current element is greater than the next element. If it is, it swaps them. If the current index is odd, it checks if the current element is less than the next element. If it is, it swaps them.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/WiggleSort.java]
```