---
b: https://blendedfeelings.com/software/data-structures/disjoint-set-data-structure.md
---

# Disjoint Set 
also known as Union-Find, is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets. It is particularly useful for keeping track of the connected components in an undirected graph and is commonly used in algorithms that need to keep track of such partitions, like Kruskal's algorithm for finding the minimum spanning tree of a graph.

The Disjoint Set data structure provides two primary operations:

1. **Find**: Determine which subset a particular element is in. This can be used for determining if two elements are in the same subset.

2. **Union**: Join two subsets into a single subset.

Here is a basic representation of the Disjoint Set data structure using Python:

```python
class DisjointSet:
    def __init__(self, size):
        # Initialize an array to hold the parent of each element.
        # Initially, each element is its own parent, representing
        # a unique set.
        self.parent = [i for i in range(size)]

    def find(self, x):
        # Find the root of the set that x belongs to.
        if self.parent[x] != x:
            # Path compression: update the parent of x to be the
            # root of the set, to flatten the structure.
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find the roots of the sets that x and y belong to.
        root_x = self.find(x)
        root_y = self.find(y)

        # If x and y are already in the same set, do nothing.
        if root_x == root_y:
            return

        # Otherwise, make one root the parent of the other, effectively
        # merging the two sets.
        self.parent[root_y] = root_x

# Example usage:
ds = DisjointSet(10)  # Create a Disjoint Set with 10 elements
ds.union(1, 2)        # Merge the sets that contain 1 and 2
ds.union(3, 4)        # Merge the sets that contain 3 and 4
print(ds.find(1) == ds.find(2))  # Should print True, as 1 and 2 are in the same set
print(ds.find(1) == ds.find(3))  # Should print False, as 1 and 3 are in different sets
```

In this implementation, we also use a technique called "path compression" in the `find` method, which flattens the structure of the tree, ensuring that each node points directly to the root of the set. This optimization helps to keep the trees representing the sets shallow, which leads to very efficient `find` and `union` operations.

The Disjoint Set data structure can be further optimized by using "union by rank" or "union by size," where the root of the smaller set is made a child of the root of the larger set. This optimization can help to keep the tree even more balanced, which can improve the time complexity of the operations to nearly constant time, i.e., \(O(\alpha(n))\), where \(\alpha\) is the inverse Ackermann function, which grows very slowly and is practically constant for all reasonable input sizes.