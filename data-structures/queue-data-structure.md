---
b: https://blendedfeelings.com/software/data-structures/queue-data-structure.md
---

# Queue 
is a linear data structure that follows the First-In-First-Out (FIFO) principle. This means that the first element added to the queue will be the first one to be removed. It is an abstract data type with the following main operations:

1. **Enqueue**: Add an element to the back of the queue.
2. **Dequeue**: Remove an element from the front of the queue.
3. **Front** (or **Peek**): Look at the front element of the queue without removing it.
4. **IsEmpty**: Check if the queue is empty.
5. **Size**: Get the number of elements in the queue.

Queues are commonly used in scenarios where you need to manage objects in the order they were created or received. Examples include managing a line of customers, task scheduling, and breadth-first search algorithms in computing.

Here is a simple example of a queue implementation in C#:

```csharp
using System;
using System.Collections.Generic;

public class Queue<T>
{
    private LinkedList<T> list = new LinkedList<T>();

    // Enqueue method to add an element to the end of the queue
    public void Enqueue(T value)
    {
        list.AddLast(value);
    }

    // Dequeue method to remove and return the element at the beginning of the queue
    public T Dequeue()
    {
        if (list.Count == 0)
        {
            throw new InvalidOperationException("The queue is empty");
        }
        T value = list.First.Value;
        list.RemoveFirst();
        return value;
    }

    // Peek method to look at the element at the beginning of the queue without removing it
    public T Peek()
    {
        if (list.Count == 0)
        {
            throw new InvalidOperationException("The queue is empty");
        }
        return list.First.Value;
    }

    // IsEmpty method to check if the queue is empty
    public bool IsEmpty()
    {
        return list.Count == 0;
    }

    // Size method to get the number of elements in the queue
    public int Size()
    {
        return list.Count;
    }
}

// Example usage:
public class Program
{
    public static void Main()
    {
        Queue<int> queue = new Queue<int>();
        queue.Enqueue(1);
        queue.Enqueue(2);
        queue.Enqueue(3);
        
        Console.WriteLine(queue.Dequeue()); // Outputs 1
        Console.WriteLine(queue.Peek());    // Outputs 2
        Console.WriteLine(queue.IsEmpty()); // Outputs False
        Console.WriteLine(queue.Size());    // Outputs 2
    }
}
```

In this example, a `Queue` class is defined using a `LinkedList<T>` to store the elements. The `Enqueue` method adds an element to the end of the list, while `Dequeue` removes the element from the beginning. The `Peek` method allows us to look at the first element without removing it, `IsEmpty` checks if the queue has any elements, and `Size` returns the number of elements in the queue.