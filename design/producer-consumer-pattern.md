---
b: https://blendedfeelings.com/software/design/producer-consumer-pattern.md
---

# Producer-Consumer pattern
is a classic design pattern that deals with concurrency and synchronization in multi-threaded programming. It's used to solve problems where one set of threads (the producers) are generating data and placing it into a shared data structure, while another set of threads (the consumers) are taking the data from that structure and processing it.

The shared data structure is often a queue, where producers put items at one end (enqueue), and consumers take items from the other end (dequeue). This pattern is useful when the rate of data production does not match the rate of data consumption, requiring a buffer that can temporarily hold the data.

Here's an overview of how the Producer-Consumer pattern typically works:

**Producer**
1. The producer creates a new data item to be processed.
2. It acquires a lock on the shared data structure.
3. If the shared data structure is full, the producer waits until there is space available.
4. Once there is space, the producer adds the new item to the data structure.
5. The producer releases the lock.
6. It notifies the consumer(s) that a new item is available, if necessary.

**Consumer**
1. The consumer waits for an item to become available in the shared data structure.
2. It acquires a lock on the shared data structure.
3. If the shared data structure is empty, the consumer waits until an item is available.
4. Once an item is available, the consumer removes it from the data structure.
5. The consumer releases the lock.
6. It processes the retrieved item.

**Synchronization Mechanisms**
To prevent race conditions and ensure thread safety, several synchronization mechanisms can be used, such as:
- Mutexes/Semaphores: To ensure that only one thread can access the shared data structure at a time.
- Condition Variables: To allow threads to wait for certain conditions (e.g., non-empty queue for consumers, non-full queue for producers) to be met before proceeding.

```java
class MyClass
{
    Array buffer = new Array();

    void Producer()
    {
        while(true) 
        {
            data = GenerateData()
            buffer.Add(data)
        }
    }

    void Consumer()
    {
        while (true)
        {
            if (buffer.Length > 0) {
                data = buffer.Remove()
                ProcessData(data)
            }
        }
    }
}
```