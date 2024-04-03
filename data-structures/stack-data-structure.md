---
b: https://blendedfeelings.com/software/data-structures/stack-data-structure.md
---

# Stack 
is a linear data structure that follows the Last In, First Out (LIFO) principle. The last element added to the stack will be the first one to be removed. This is analogous to a stack of plates or books; you can only take the top item off the stack without disturbing the others.

Here are the main operations that can be performed on a stack:

1. **Push**: Add an element to the top of the stack.
2. **Pop**: Remove the element from the top of the stack and return it.
3. **Peek** or **Top**: Return the element at the top of the stack without removing it.
4. **IsEmpty**: Check if the stack is empty.
5. **Size**: Return the number of elements in the stack.

Here is a simple implementation of a stack in C#:

```csharp
public class Stack<T>
{
    private LinkedList<T> list = new LinkedList<T>();

    // Add an element to the top of the stack
    public void Push(T value)
    {
        list.AddFirst(value);
    }

    // Remove and return the top element of the stack
    public T Pop()
    {
        if (list.Count == 0)
        {
            throw new InvalidOperationException("The stack is empty");
        }
        T value = list.First.Value;
        list.RemoveFirst();
        return value;
    }

    // Return the top element of the stack without removing it
    public T Peek()
    {
        if (list.Count == 0)
        {
            throw new InvalidOperationException("The stack is empty");
        }
        return list.First.Value;
    }

    // Check if the stack is empty
    public bool IsEmpty()
    {
        return list.Count == 0;
    }

    // Return the number of elements in the stack
    public int Size()
    {
        return list.Count;
    }
}
```

This implementation uses a `LinkedList<T>` to store the elements. The `Push` operation adds a new element to the beginning of the linked list, the `Pop` operation removes the first element, and the `Peek` operation retrieves the first element without removing it. The `IsEmpty` and `Size` methods are used to check if the stack is empty and to get the number of elements, respectively.