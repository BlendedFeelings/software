---
b: https://blendedfeelings.com/software/data-structures/k-d-tree-data-structure.md
---

# K-d tree 
(short for k-dimensional tree) is a space-partitioning data structure for organizing points in a k-dimensional space. k-d trees are useful for several applications, such as searches involving a multidimensional search key (e.g., range searches and nearest neighbor searches). They were invented in 1975 by Jon Bentley.

The main idea of a k-d tree is that it recursively subdivides the space into two half-spaces at each level of the tree. Here's a brief overview of how a k-d tree is structured and how it works:

### Structure of a k-d Tree:
- **Nodes**: Each node in a k-d tree represents a point in k-dimensional space.
- **Splitting Dimension**: At each level of the tree, a dimension is chosen to split the space. This dimension cycles through all k dimensions as we move down the tree.
- **Splitting Value**: The value in the chosen dimension that splits the space into two halves. The actual point that determines this value becomes the node for that level of the tree.

### Building a k-d Tree:
1. Select the dimension for splitting, usually starting with the first dimension and cycling through to the k-th dimension as you go down each level of the tree.
2. Find the median value in the selected dimension among the points. This median point becomes the node at this level.
3. Partition the point set into two subsets: one with points less than the median in the splitting dimension, and the other with points greater than or equal to the median.
4. Recursively repeat the process on each subset for the next dimension.

### Operations on a k-d Tree:
- **Insertion**: To insert a point, traverse the tree according to the splitting dimensions and values until you find an appropriate leaf node where the new point should be inserted.
- **Deletion**: To delete a point, find the node, remove it, and then restructure the tree to maintain its properties.
- **Search**: To find a point, traverse the tree based on the splitting dimensions and values, much like a binary search tree.
- **Range Search**: To find all points within a certain range, traverse the tree and collect all points that fall within the specified range.
- **Nearest Neighbor Search**: To find the closest point to a given point, traverse the tree to find the best candidate and then backtrack to ensure that there are no closer points in the other branches of the tree.

### Properties of k-d Trees:
- The tree is balanced if built using the median value at each level.
- The tree's height is O(log n) if balanced, where n is the number of points.
- Nearest neighbor searches can be performed efficiently if the tree is balanced.

### Limitations of k-d Trees:
- They do not handle dynamically changing datasets well, as frequent insertions and deletions can unbalance the tree.
- They are not well-suited for high-dimensional spaces (the so-called "curse of dimensionality"), as the efficiency of nearest neighbor searches degrades in such cases.

k-d trees are widely used in computer graphics for tasks such as ray tracing, and in machine learning for nearest neighbor queries, among other applications.