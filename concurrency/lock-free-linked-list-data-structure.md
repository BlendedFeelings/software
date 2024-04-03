---
b: https://blendedfeelings.com/software/concurrency/lock-free-linked-list-data-structure.md
---

# Lock-free linked list 
is a concurrent data structure that allows multiple threads to insert, delete, and access elements without the need for traditional locking mechanisms, such as mutexes or semaphores. The goal of lock-free data structures is to achieve better scalability and avoid problems like deadlocks, priority inversion, and convoying that can occur with lock-based synchronization.

Lock-free algorithms typically rely on atomic operations provided by modern CPUs, such as Compare-And-Swap (CAS), Load-Link/Store-Conditional (LL/SC), or similar instructions that can be used to ensure that updates to shared data are done atomically, without interference from other threads.

Here's a simplified conceptual example of a lock-free singly linked list node in C++:

```cpp
#include <atomic>

template <typename T>
class LockFreeListNode {
public:
    T value;
    std::atomic<LockFreeListNode<T>*> next;

    LockFreeListNode(T val) : value(val), next(nullptr) {}
};

template <typename T>
class LockFreeLinkedList {
private:
    std::atomic<LockFreeListNode<T>*> head;

public:
    LockFreeLinkedList() : head(nullptr) {}

    void insert(const T& value) {
        LockFreeListNode<T>* newNode = new LockFreeListNode<T>(value);
        newNode->next = head.load(std::memory_order_relaxed);

        while (!head.compare_exchange_weak(newNode->next, newNode,
                                           std::memory_order_release,
                                           std::memory_order_relaxed)) {
            // Loop until the head is updated with the new node
        }
    }

    bool remove(const T& value) {
        LockFreeListNode<T>* pred;
        LockFreeListNode<T>* curr;
        LockFreeListNode<T>* succ;

        do {
            pred = head.load(std::memory_order_relaxed);
            curr = pred;

            while (curr != nullptr) {
                succ = curr->next.load(std::memory_order_relaxed);

                if (curr->value == value) {
                    if (!pred->next.compare_exchange_weak(curr, succ,
                                                          std::memory_order_release,
                                                          std::memory_order_relaxed)) {
                        break; // Failed to remove, retry
                    }

                    delete curr; // Successfully removed
                    return true;
                }

                pred = curr;
                curr = succ;
            }
        } while (curr != nullptr);

        return false; // Value not found
    }

    // Additional methods such as search, etc. can be implemented similarly
};
```

Please note that this is a simplified example. A real-world lock-free linked list would need to handle more complex scenarios, such as the ABA problem, where a node is removed and then a new node with the same address is inserted between the time a pointer is read and the time an update is attempted. This can be addressed by using a double-word CAS that also checks a version number or by using hazard pointers or other safe memory reclamation techniques.

Lock-free programming is an advanced topic and requires a good understanding of memory models, processor architectures, and concurrent programming. It's recommended to use well-tested lock-free data structures from libraries or language runtimes when possible, as writing correct lock-free code is quite challenging.