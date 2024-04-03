---
b: https://blendedfeelings.com/software/data-structures/r-tree-data-structure.md
---

# R-tree 
is a tree data structure used for indexing multi-dimensional information such as geographical coordinates, rectangles, and polygons. The structure is designed to efficiently handle spatial queries such as "Which objects intersect with this given area?" It was proposed by Antonin Guttman in 1984 and has been widely used in geographic information systems (GIS), spatial databases, and for various applications that involve multi-dimensional keys.

Here's a brief overview of the properties and operations of an R-tree:

### Properties of R-trees:

1. **Hierarchical Structure**: An R-tree is a balanced tree similar to a B-tree, with leaf and internal nodes.
2. **Bounding Rectangles**: Each node contains entries that represent bounding rectangles (or sometimes bounding boxes in 3D space) that cover all objects in its child nodes.
3. **Variable Node Capacity**: Each node can hold a variable number of entries up to a maximum defined by the parameter `M`. The minimum number of entries for a node, except for the root, is typically set to `m = ⌈M/2⌉`.
4. **Leaf Nodes**: Leaf nodes contain entries that point to the actual spatial objects (e.g., rectangles, points, polygons).
5. **Internal Nodes**: Internal nodes contain entries that point to their child nodes, with each entry representing the minimum bounding rectangle (MBR) that encompasses all the rectangles in the child node.

### Operations on R-trees:

1. **Insertion**: To insert a new entry, the tree is traversed from the root to find the most appropriate leaf node, ensuring that the area of the bounding rectangles is minimally increased. If a node overflows (i.e., has more entries than `M`), it is split into two nodes.
2. **Deletion**: To delete an entry, the tree is traversed to find the entry, which is then removed. The tree may need to be restructured to maintain its properties.
3. **Search**: To search for all entries that intersect with a given query rectangle, the tree is traversed starting from the root, recursively visiting child nodes that intersect with the query rectangle.
4. **Nearest Neighbor Search**: To find the nearest neighbor to a point, a priority queue can be used to perform a best-first search.

### Variants of R-trees:

There are several variants of the original R-tree that aim to improve its performance in certain aspects:

- **R+ Tree**: Disallows overlapping bounding rectangles among sibling nodes.
- **R* Tree**: Adjusts the tree by reinserting elements and choosing split points to minimize overlap, coverage, and margin of bounding boxes.
- **Hilbert R-tree**: Uses the Hilbert space-filling curve to impose a linear ordering on the entries in the tree.

R-trees are particularly well-suited for disk-based storage systems where the minimization of disk reads is important. They are designed to minimize the bounding rectangle overlap, which reduces the number of nodes that need to be visited during search operations.