---
b: https://blendedfeelings.com/software/data-structures/segment-tree-data-structure.md
---

# Segment Tree 
is a versatile data structure that is used to store information about intervals, or segments. It allows querying which segments contain a certain point, or the sum of elements within a range, efficiently. Segment Trees are particularly useful in scenarios where there are many range queries on an array and the array is not updated frequently, as they can answer these queries in logarithmic time.

Here's a high-level overview of a Segment Tree:

1. **Structure**: It is a binary tree where each node stores information about a segment of the array. The root represents the entire array, and each leaf represents a single element. The internal nodes represent the union of their children's segments.

2. **Building**: A Segment Tree for an array can be built in *O(n log n)* time. The tree is built recursively: the root node represents the entire array, and each subsequent level halves the segments until individual elements are reached at the leaves.

3. **Querying**: The tree supports range queries, such as finding the sum or minimum/maximum of elements within a given range. This is done in *O(log n)* time by traversing the tree from the root to the leaves, visiting only the nodes that intersect with the query range.

4. **Updating**: Segment Trees can be updated when an element in the array changes. The update operation also takes *O(log n)* time, as it requires updating the leaf corresponding to the element and all of its ancestor nodes up to the root.

Here's a simple example of how a Segment Tree might be structured for sum queries:

```
Array: [1, 3, 5, 7, 9, 11]
Segment Tree:
                  [1, 6] (Sum=36)
                 /       \
         [1, 3] (Sum=9)   [4, 6] (Sum=27)
        /       \           /      \
  [1, 2] (Sum=4) [3] (Sum=5) [4, 5] (Sum=16) [6] (Sum=11)
  /     \                     /     \
[1] (1) [2] (3)             [4] (7) [5] (9)
```

In this example, each node is labeled with the range of indices it covers and the sum of that range. To query the sum of elements from index 2 to 5, the tree would combine the results from nodes [2] (3), [3] (5), and [4, 5] (16) for a total of 24.

Implementing a Segment Tree involves writing methods for building the tree, querying the tree, and updating the tree. The specific implementation details can vary depending on the type of query the tree is intended to support (e.g., sum, minimum, maximum).

Segment Trees can be extended to support more complex operations and can be modified to become Lazy Segment Trees, which allow for range updates in addition to range queries.