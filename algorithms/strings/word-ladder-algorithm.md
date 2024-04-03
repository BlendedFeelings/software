---
b: https://blendedfeelings.com/software/algorithms/strings/word-ladder-algorithm.md
---

# WordLadder
is a word game where the player is given two words of equal length and is required to transform one word into the other by changing one letter at a time. Each intermediate word formed must be a valid word in the dictionary. The goal is to find the shortest possible sequence of words that transforms the starting word into the target word. 

**Example 1:**
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog",
which is 5 words long.

**Example 2:**
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation
sequence.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/strings/WordLadder.java]
```