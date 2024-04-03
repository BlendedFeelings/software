---
b: https://blendedfeelings.com/software/algorithms/searche/monte-carlo-tree-search-algorithm.md
---

# Monte Carlo Tree Search (MCTS)
is a heuristic search algorithm that is commonly used in artificial intelligence for decision-making processes. It is particularly useful in games and other complex decision-making scenarios where the search space is too large to explore exhaustively.

MCTS works by constructing a tree of possible moves and outcomes, and then simulating random games from each node in the tree to estimate the likelihood of winning from that position. This process is repeated many times, with the results of each simulation being used to update the estimated win probabilities for each node in the tree.

Over time, MCTS focuses its search on the most promising branches of the tree, leading to better and better estimates of the optimal move. This makes it a powerful tool for decision-making in complex environments.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/searches/MonteCarloTreeSearch.java]
```