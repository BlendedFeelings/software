---
b: https://blendedfeelings.com/software/algorithms/sort/topological-sort-algorithm.md
---

# Topological Sort 
is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge (u, v), vertex u comes before vertex v in the ordering. In other words, it is a way of arranging the nodes of a graph in a linear order such that all the dependencies of a node come before the node itself.

Topological Sort is useful in many applications such as task scheduling, dependency resolution, and job sequencing. It can be implemented using Depth First Search (DFS) algorithm.

The algorithm works as follows:
1. Perform a DFS traversal of the graph.
2. When a vertex is visited, mark it as visited and add it to a stack.
3. When all the adjacent vertices of a vertex have been visited, add the vertex to the stack.
4. The topological sort is the reverse order of the vertices in the stack.

If the graph contains a cycle, then it is not possible to perform a topological sort.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/sorts/TopologicalSort.java]
```