---
b: https://blendedfeelings.com/software/algorithms/searche/binary-search-algorithm.md
---

# Binary Search 
is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item until you've narrowed the possible locations to just one.

Here is how the binary search algorithm works:

1. Find the middle element of the array.
2. If the middle element is equal to the target value, return the index of the middle element.
3. If the middle element is less than the target value, then the target must be in the right half of the array. Discard the left half by adjusting the starting index.
4. If the middle element is greater than the target value, then the target must be in the left half of the array. Discard the right half by adjusting the ending index.
5. Repeat the process on the new half-array until the target is found or the subarray has size 0 (meaning the element is not in the array).


```csharp
public int BinarySearch(int[] array, int target)
{
    int left = 0;
    int right = array.Length - 1;

    while (left <= right

```java
[!INCLUDE https://github.com/thealgorithms/java/blob/master/src/main/java/com/thealgorithms/searches/BinarySearch.java]
```