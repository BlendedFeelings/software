---
b: https://blendedfeelings.com/software/algorithms/sort/tim-sort-algorithm.md
---

# TimSort
is a sorting algorithm that is a hybrid of merge sort and insertion sort. It was designed to perform well on many kinds of real-world data. 

The algorithm works by dividing the input array into small chunks, called runs, and sorting them using insertion sort. The runs are then merged using a modified merge sort algorithm. The modification is that it takes advantage of the partially sorted runs to reduce the number of comparisons needed to merge them.

The algorithm has a best-case time complexity of O(n), where n is the number of elements to be sorted. Its worst-case time complexity is O(n log n), which is the same as merge sort. However, in practice, TimSort performs better than merge sort on many types of data because it takes advantage of pre-existing order in the data.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/TimSort.java]
```