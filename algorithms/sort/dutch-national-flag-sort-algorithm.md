---
b: https://blendedfeelings.com/software/algorithms/sort/dutch-national-flag-sort-algorithm.md
---

# Dutch National Flag (DNF)
is a sorting algorithm designed to sort an array of elements that have three possible values, such as 0, 1, and 2. It was named after the flag of the Netherlands, which has three horizontal bands of red, white, and blue.

The algorithm works by maintaining three pointers, low, mid, and high, which divide the array into four sections:

Elements less than the pivot (0) are to the left of the low pointer.
Elements greater than the pivot (2) are to the right of the high pointer.
Elements equal to the pivot are between the low and mid pointers.
Unexplored elements are between the mid and high pointers.
The algorithm then performs a linear scan of the array and swaps elements as necessary to maintain the four sections.

This algorithm is efficient because it only needs to scan the array once, and it sorts the array in-place without using any extra memory.


```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/DutchNationalFlagSort.java]
```