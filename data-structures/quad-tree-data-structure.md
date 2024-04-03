---
b: https://blendedfeelings.com/software/data-structures/quad-tree-data-structure.md
---

# Quadtree 
is a tree data structure in which each internal node has exactly four children. Quadtrees are most often used to partition a two-dimensional space by recursively subdividing it into four quadrants or regions. They are the two-dimensional analog of octrees and are related to binary trees.

Quadtrees are used in various applications, such as in image processing for spatial indexing, efficient collision detection in two dimensions, storing sparse data (like a sparse matrix), and in games for areas like terrain generation and management.

Here’s a basic idea of how a quadtree might be structured:

1. **Node**: Each node in a quadtree represents a rectangular bounding box covering part of the space being indexed. Each node stores pointers to its four children, which represent the four quadrants of the space covered by their parent node.

2. **Quadrants**: The space covered by a quadtree node is divided into four quadrants, typically labeled as:
   - North-West (NW)
   - North-East (NE)
   - South-West (SW)
   - South-East (SE)

3. **Leaves**: The leaves of a quadtree (nodes with no children) represent individual units of space that are not further subdivided. These could correspond to pixels in an image, for example.

4. **Insertion**: To insert an item, you start at the root and recursively descend through the children corresponding to the quadrant where the item belongs until you reach a leaf node. If the leaf node becomes too crowded (i.e., contains more items than a predefined maximum), it is subdivided and the items are distributed among the new children.

5. **Search**: To search for items in a quadtree, you start at the root and recursively check each child node to see if it intersects with the search area. If it does, the search continues into that child node; if not, the search can skip that part of the tree.

Here is a simple conceptual representation of a quadtree node in pseudocode:

```pseudocode
class QuadTreeNode:
    def __init__(self, boundary):
        self.boundary = boundary  # The rectangular region covered by this node
        self.children = [None, None, None, None]  # Pointers to NW, NE, SW, SE children
        self.data = []  # Data contained in this node (e.g., points, objects)

    def subdivide(self):
        # Subdivide the node into four children
        ...

    def insert(self, item):
        # Insert an item into the quadtree, subdivide if necessary
        ...

    def query_range(self, range):
        # Return all items that fall within the given range
        ...
```

The actual implementation of these methods would depend on the specific use case and requirements, such as how to handle items that overlap quadrant boundaries, how to define the maximum capacity of a leaf node, and how to handle dynamic changes to the indexed space.