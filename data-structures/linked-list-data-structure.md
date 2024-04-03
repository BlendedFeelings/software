---
b: https://blendedfeelings.com/software/data-structures/linked-list-data-structure.md
---

# Linked list 
is a linear data structure where each element is a separate object, commonly called a "node." Each node contains two items: the data itself and a reference (or a "link") to the next node in the sequence. This structure allows for efficient insertion and removal of elements from any position in the sequence during iteration.

Here's a simple representation of a singly linked list node in C#:

```csharp
public class ListNode<T>
{
    public T Data { get; set; }
    public ListNode<T> Next { get; set; }

    public ListNode(T data)
    {
        Data = data;
        Next = null;
    }
}
```

In a singly linked list, each node points to the next node in the list. The first node is called the "head" of the list, and the last node, which points to `null`, is called the "tail."

There are also doubly linked lists, where each node has a reference to both the next and the previous node:

```csharp
public class DoublyListNode<T>
{
    public T Data { get; set; }
    public DoublyListNode<T> Next { get; set; }
    public DoublyListNode<T> Prev { get; set; }

    public DoublyListNode(T data)
    {
        Data = data;
        Next = null;
        Prev = null;
    }
}
```

In a doubly linked list, you can traverse the list in both directions: forward and backward. This makes operations like deletion more efficient because you can access the previous node directly without having to traverse the list from the head to find it.

The main advantage of linked lists over arrays is that the elements are linked using pointers, so the list can expand or shrink in size dynamically without the need for reallocation or reorganization of the entire structure, as would be necessary with an array.

However, linked lists have some drawbacks compared to arrays, such as the lack of direct access to elements by index, which means that accessing an element has a time complexity of O(n) where n is the position of the element in the list. Additionally, linked lists typically use more memory than arrays because of the storage required for the references/pointers.