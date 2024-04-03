---
b: https://blendedfeelings.com/software/algorithms/strings/aho-corasick-algorithm.md
---

# Aho-Corasick
is a string searching algorithm that efficiently searches for multiple patterns in a given text. It was developed by Alfred V. Aho and Margaret J. Corasick in 1975. 

The algorithm constructs a finite state machine that represents all the patterns to be searched. The machine is constructed in a way that allows it to efficiently search for all patterns in a single pass over the text. 

The algorithm works by first constructing a trie (a tree-like data structure) of all the patterns to be searched. Then, it adds failure links to the trie to allow it to efficiently transition between states when a match is not found. Finally, it adds output links to the trie to allow it to output all patterns that match at a given position in the text.

When searching for patterns in a text, the algorithm starts at the root of the trie and transitions through the states based on the characters in the text. If a match is found, the algorithm outputs the pattern and continues searching for other patterns. If a match is not found, the algorithm follows the failure links to transition to a new state and continue searching.

The Aho-Corasick algorithm has a time complexity of O(n + m + z), where n is the length of the text, m is the total length of all patterns, and z is the number of matches found. This makes it a very efficient algorithm for searching for multiple patterns in a text.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/strings/AhoCorasick.java]
```