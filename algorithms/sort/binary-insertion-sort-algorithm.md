---
b: https://blendedfeelings.com/software/algorithms/sort/binary-insertion-sort-algorithm.md
---

# Binary Insertion Sort
is a variation of Insertion Sort algorithm where the proper location to insert the selected element is found using the binary search algorithm instead of the linear search algorithm used in the traditional Insertion Sort algorithm. This algorithm works by dividing the input array into two parts: sorted and unsorted. Initially, the sorted part contains only the first element of the array, and the unsorted part contains the remaining elements. Then, for each element in the unsorted part, the algorithm finds its proper position in the sorted part using binary search and inserts it there. This process is repeated until the entire array is sorted.

The advantage of using Binary Insertion Sort over the traditional Insertion Sort algorithm is that it reduces the number of comparisons needed to insert an element into its proper position, which results in a faster sorting time. However, the algorithm still has a worst-case time complexity of O(n^2) like the traditional Insertion Sort algorithm.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/BinaryInsertionSort.java]
```