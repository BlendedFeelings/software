---
b: https://blendedfeelings.com/software/algorithms/strings/longest-non-repeative-substring-algorithm.md
---

# Longest Non Repeative Substring
takes a string as input and returns the length of the longest non-repeating substring in the input string. The algorithm uses a sliding window approach to keep track of the current substring and a dictionary to keep track of the last index of each character seen in the substring. If a character is seen again, the start of the substring is moved to the next index after the last occurrence of the character. The length of the longest substring seen so far is updated at each iteration.

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/strings/longestNonRepeativeSubstring.java]
```