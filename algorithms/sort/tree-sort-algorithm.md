---
b: https://blendedfeelings.com/software/algorithms/sort/tree-sort-algorithm.md
---

# TreeSort
is a sorting algorithm that works by first building a binary search tree from the elements to be sorted, and then traversing the tree in-order to obtain the sorted sequence. 

The algorithm works as follows:
1. Create an empty binary search tree.
2. Insert each element of the input sequence into the binary search tree.
3. Traverse the binary search tree in-order, and output each element as it is visited.

The time complexity of TreeSort is O(n log n) in the average case, and O(n^2) in the worst case if the input sequence is already sorted. However, the worst case can be avoided by using a self-balancing binary search tree, such as an AVL tree or a red-black tree, which ensures that the height of the tree is always logarithmic in the number of elements.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/TreeSort.java]
```