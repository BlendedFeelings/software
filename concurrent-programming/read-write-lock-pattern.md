---
b: https://blendedfeelings.com/software/concurrent-programming/read-write-lock-pattern.md
---

# Read-Write Lock Pattern
 is a concurrency control pattern used in computing to improve performance when a data structure is read frequently but written to infrequently. It is designed to allow multiple threads to read a data structure concurrently, but only one thread to write to it at a time, thus ensuring data consistency and preventing race conditions.

Here's a high-level overview of how the Read-Write Lock pattern works:

- **Read Locks (Shared Locks):** Multiple threads can acquire read locks simultaneously, as long as there is no thread holding a write lock. This allows for concurrent read-only access to the resource.

- **Write Locks (Exclusive Locks):** Only one thread can acquire a write lock at a time. When a thread holds a write lock, no other thread can acquire a read lock or a write lock. This ensures that the thread can modify the resource without interference from other threads.

- **Lock Upgrade:** A thread holding a read lock may request an upgrade to a write lock. However, the upgrade is not usually immediate and may require the thread to release the read lock and wait until it can acquire a write lock.

- **Lock Downgrade:** A thread holding a write lock may downgrade it to a read lock, which can be useful when a thread finishes writing and moves to a read-only operation.

```java
class MyList {
    ReadWriteLock lock = new ReentrantReadWriteLock();
    List<String> list = new ArrayList<>();

    void add(String item) {
        Lock writeLock = lock.writeLock();
        writeLock.lock();
        try {
            list.add(item);
        } finally {
            writeLock.unlock();
        }
    }

    String get(int index) {
        Lock readLock = lock.readLock();
        readLock.lock();
        try {
            return list.get(index);
        } finally {
            readLock.unlock();
        }
    }

    int size() {
        Lock readLock = lock.readLock();
        readLock.lock();
        try {
            return list.size();
        } finally {
            readLock.unlock();
        }
    }
}

```