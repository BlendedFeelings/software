---
b: https://blendedfeelings.com/software/conflict-free-replicated-data-types/observed-removed-set.md
---

# OR-Set, or Observed-Removed Set, 
is a data structure that is part of the Conflict-Free Replicated Data Types (CRDTs) family, which are used to build distributed systems that can operate effectively in environments with intermittent connectivity and where different replicas of the data might diverge.

The OR-Set is designed to allow for the addition and removal of elements in a way that ensures eventual consistency across all replicas without the need for complex conflict resolution. This is particularly useful in scenarios where operations may not happen in a well-defined order, such as distributed databases or collaborative applications.

Here's how an OR-Set typically works:

1. **Addition of Elements**: When an element is added to the set, it is tagged with a unique identifier (UID). This UID is often a combination of a unique element identifier and a unique replica identifier (such as a timestamp or a sequence number).

2. **Removal of Elements**: When an element is removed, the operation doesn't just remove the element; it records the UID of the element being removed. This way, if the same element is concurrently added on another replica, the system can distinguish between the two instances.

3. **Lookup**: To determine if an element is in the set, the OR-Set checks if there is an add operation for that element without a corresponding remove operation.

4. **Merging**: When replicas synchronize with each other, they merge their sets by taking the union of all added elements and the union of all removed UIDs. This way, all operations are preserved, and the system can correctly determine the state of the set.

The design of the OR-Set ensures that additions and removals are idempotent (applying them multiple times does not change the result) and commutative (they can be applied in any order and still yield the same result), which are key properties for achieving eventual consistency in distributed systems.

An important aspect of OR-Sets is that they can handle the issue of "add-remove-add" scenarios. If an element is added, removed, and then added again, the new addition will have a different UID, allowing the set to distinguish it from the previous addition and removal.

Here's a simplified example of how an OR-Set might be represented:

```python
# A simple representation of an OR-Set
or_set = {
    'elements': {
        'a': [('a', 1)],  # The element 'a' with UID ('a', 1)
        'b': [('b', 2)],  # The element 'b' with UID ('b', 2)
    },
    'tombstones': set(),  # Removed UIDs will be stored here
}

# Adding an element
def add_element(or_set, element, uid):
    or_set['elements'].setdefault(element, []).append(uid)

# Removing an element
def remove_element(or_set, element, uid):
    or_set['elements'].pop(element, None)
    or_set['tombstones'].add(uid)

# Checking if an element exists
def element_exists(or_set, element):
    return element in or_set['elements'] and not or_set['elements'][element] in or_set['tombstones']

# Merging two OR-Sets
def merge_or_sets(or_set1, or_set2):
    for element, uids in or_set2['elements'].items():
        for uid in uids:
            add_element(or_set1, element, uid)
    or_set1['tombstones'].update(or_set2['tombstones'])

# Example usage
add_element(or_set, 'c', ('c', 3))
remove_element(or_set, 'a', ('a', 1))
print(element_exists(or_set, 'a'))  # False
print(element_exists(or_set, 'b'))  # True
```

This is a very basic representation and doesn't cover all the intricacies of an OR-Set in a distributed system, but it gives a general idea of how it functions. In a real-world implementation, the UIDs would be more complex, and additional mechanisms would be in place to handle concurrent updates and merges more efficiently.