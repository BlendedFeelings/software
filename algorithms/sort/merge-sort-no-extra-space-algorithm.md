---
b: https://blendedfeelings.com/software/algorithms/sort/merge-sort-no-extra-space-algorithm.md
---

# Merge Sort No Extra Space
is a variant of MergeSort that sorts the list in-place, without using any additional memory. This is achieved by modifying the merge step of the algorithm to use a cyclic swapping technique instead of creating a new list to store the merged elements. The cyclic swapping technique involves shifting the elements in the list to the right by one position and inserting the merged element in the first position of the list. This process is repeated until all the elements are merged.

The MergeSortNoExtraSpace algorithm has a space complexity of O(1) and a time complexity of O(n log n), where n is the number of elements in the list. However, the algorithm can be slower than the standard MergeSort algorithm due to the additional overhead of the cyclic swapping technique.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/MergeSortNoExtraSpace.java]
```