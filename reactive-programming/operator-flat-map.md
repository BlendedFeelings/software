---
b: https://blendedfeelings.com/software/reactive-programming/operator-flat-map.md
---

# Operator FlatMap
is used to transform the items emitted by an `Observable` (or any other reactive stream type, depending on the library/framework) into `Observables` themselves, and then flatten the emissions from those into a single `Observable`.

The `FlatMap` operator works as follows:

1. It applies a function to each item emitted by the source `Observable`.
2. This function returns an `Observable` for each item.
3. Instead of emitting these `Observables` directly, `FlatMap` merges all of these separate `Observables` and emits their emissions as a single `Observable`.

The emissions from the resulting `Observables` can interleave, meaning that `FlatMap` does not guarantee the order of the items. If order is important, you might use `ConcatMap` or `SwitchMap`, which provide different ways of handling the order and concurrency of the resulting `Observables`.

Here is a simple conceptual example in pseudo-code:

```pseudo
sourceObservable = Observable.of(1, 2, 3)

// Function that maps each number to an Observable that emits values (number, number+1)
func mapToObservable(number) {
    return Observable.of(number, number+1)
}

flattenedObservable = sourceObservable.flatMap(mapToObservable)

// The flattenedObservable will emit: 1, 2, 2, 3, 3, 4
```

In practice, `FlatMap` is often used when you have a sequence of items and you want to asynchronously fetch more data based on each item, then combine all the data back into a single stream. For example, if you have a stream of user IDs, and you want to fetch user details for each ID from a database or an API, `FlatMap` would be an appropriate choice to map each ID to a request and then merge the results into a single stream of user details.

Different reactive programming libraries might have variations on `FlatMap` with slightly different behaviors or names, but the core concept remains the same across these libraries.