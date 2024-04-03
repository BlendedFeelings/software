---
b: https://blendedfeelings.com/software/data-structures/skip-list-data-structure.md
---

# Skip list 
is a data structure that allows fast search within an ordered sequence of elements. It is a probabilistic alternative to balanced trees and is easier to implement while still providing logarithmic time complexity for most operations.

The skip list consists of multiple layers of linked lists, where each layer is a subset of the one below it. The bottom layer (Level 0) is an ordinary sorted linked list containing all the elements. Each higher layer acts as an "express lane" for the layers below, containing only a subset of the elements (those that have been "promoted"). The idea is that by jumping along higher layers, you can skip over many elements, achieving faster search times.

Here's a simplified representation of how a skip list might look:

```
Level 3:    1 --------------------------------> 9
Level 2:    1 --------> 5 --------> 9
Level 1:    1 ----> 3 ----> 5 ----> 7 ----> 9
Level 0:    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
```

Here are the basic operations of a skip list:

1. **Search**: To search for a value, you start at the highest level and move forward while the next element is less than the value you're searching for. When you can't move forward anymore, you drop down one level and continue. You repeat this until you find the value or reach the bottom level and conclude that the value is not present.

2. **Insertion**: To insert a new element, you first search for the position where it should be inserted in the bottom list. Then, you insert it there and also decide randomly if it should be promoted to the higher level. If promoted, you continue the process for each level until the promotion fails (usually by flipping a coin or using a random number generator).

3. **Deletion**: To delete an element, you search for it and remove it from all the levels in which it appears.

4. **Update**: To update a value, you delete the old value and insert the new value, ensuring that the list remains sorted.

The efficiency of a skip list depends on the number of levels and the probability used to promote nodes to higher levels. The expected time complexity for search, insertion, and deletion is O(log n), where n is the number of elements in the list. However, because it is a probabilistic structure, the worst-case time complexity can be linear, O(n), although this is very unlikely with a well-designed skip list.

Skip lists require extra memory for the pointers at higher levels, and the random nature of the structure can lead to non-optimal configurations, but in practice, skip lists perform quite well and are used in various systems, like databases and indexing services.