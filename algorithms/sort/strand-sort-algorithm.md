---
b: https://blendedfeelings.com/software/algorithms/sort/strand-sort-algorithm.md
---

# StrandSort
is a sorting algorithm that works by repeatedly pulling sorted sublists out of the unsorted list and merging them together. It was invented by Jonathan Bentley and described in a 2004 article in Dr. Dobb's Journal.

The algorithm works as follows:

1. Initialize an empty output list and an empty strand.
2. While the input list is not empty:
   a. Remove the first element from the input list and add it to the strand.
   b. For each subsequent element in the input list, if it is greater than or equal to the last element in the strand, remove it from the input list and add it to the strand. Otherwise, leave it in the input list.
   c. If the strand is now sorted, remove it from the input list and merge it into the output list. Otherwise, leave it in the input list and start a new strand.
3. Merge any remaining strands into the output list.

The algorithm is similar to insertion sort, but instead of inserting each element into its correct position in the output list, it builds sorted sublists (strands) and merges them together. It has a worst-case time complexity of O(n^2), but in practice it can be faster than other O(n^2) algorithms like bubble sort and insertion sort because it tends to create shorter strands that are easier to merge.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/StrandSort.java]
```