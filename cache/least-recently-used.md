---
b: https://blendedfeelings.com/software/cache/least-recently-used.md
---

# LRU (Least Recently Used) cache 
is a type of cache eviction algorithm that removes the least recently used items first. This is based on the assumption that items that were used recently are more likely to be used again in the near future.

Here's a basic outline of how an LRU cache works:

1. The cache has a fixed size, which determines the number of items it can hold.
2. When a new item is accessed, it is added to the cache. If the item is already in the cache, it is moved to the "most recently used" position.
3. If the cache is full and a new item needs to be added, the "least recently used" item is removed to make space for the new item.
4. The cache keeps track of the usage order of items, often by maintaining them in a linked list or using a more complex data structure that allows both fast access and order maintenance, such as a combination of a hash map and a doubly linked list.

Implementing an LRU cache typically involves two data structures:

- **Hash Map**: This allows for fast access (O(1) time complexity) to cache items by key.
- **Doubly Linked List**: This maintains the order of items based on their usage, with the most recently used items at the head of the list and the least recently used items at the tail.

Here's a simple implementation of an LRU cache in Python:

```python
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.recently_used = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.recently_used.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.recently_used.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                oldest = self.recently_used.popitem(last=False)
                self.cache.pop(oldest[0])
        self.cache[key] = value
        self.recently_used[key] = None
```

In this implementation, the `OrderedDict` from the `collections` module is used to keep track of the order of items, where the most recent item is always at the end. The `get` and `put` methods are used to access and add items to the cache, respectively. If the cache reaches its capacity, the least recently used item (the first item in the `OrderedDict`) is removed.

Please note that this is a simplified version and may not be thread-safe or optimized for all use cases. For production code, additional considerations such as concurrency control and fine-tuning for performance may be necessary.