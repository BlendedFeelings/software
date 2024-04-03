---
b: https://blendedfeelings.com/software/algorithms/searche/exponential-search-algorithm.md
---

# Exponential search
is a searching algorithm that can be used to search for an element in a sorted array. It works by first finding a range in which the element might be present and then performing a binary search within that range.

The algorithm works by doubling the index value starting from 1 until the value at that index is greater than or equal to the search value. Then, it performs a binary search on the subrange from the previous index to the current index.

This algorithm has a time complexity of O(log n) and is more efficient than a simple linear search for larger arrays. However, it requires the array to be sorted in order for it to work correctly.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/searches/ExponentalSearch.java]
```