---
b: https://blendedfeelings.com/software/reactive-programming/operator-switch-map.md
---

# Operator SwitchMap
is particularly useful when you want to cancel and switch to a new Observable based on the emissions of the source Observable. The `SwitchMap` operator is commonly used in scenarios where you want to ignore the previous emissions when a new emission occurs.

Here's how the `SwitchMap` operator works:

1. When a new item is emitted by the source Observable, the `SwitchMap` operator applies a function to the item.
2. This function returns a new Observable, which is then subscribed to.
3. If the source Observable emits another item while the new Observable is still emitting items, the `SwitchMap` operator will unsubscribe from the earlier Observable and subscribe to the Observable derived from the new item.
4. This means that `SwitchMap` will always only listen to the latest Observable and will cancel any previous subscriptions to earlier Observables.

This behavior is particularly useful in scenarios such as search type-ahead, where you want to send a request to retrieve search results for every keystroke, but you only care about the results of the most recent request.

Here's an example in RxJS:

```javascript
const { of, timer } = require('rxjs');
const { switchMap, map } = require('rxjs/operators');

// Simulating a type-ahead search input that emits values at different times
const searchInput$ = of('a', 'ab', 'abc');

const result$ = searchInput$.pipe(
  // For each input value, start a new simulated HTTP request (could be replaced with an actual HTTP call)
  switchMap(input => {
    console.log(`Querying for ${input}`);
    // Simulate an HTTP request with a delay
    return timer(500).pipe(map(() => `Result for ${input}`));
  })
);

result$.subscribe(console.log);
```

In this example, even if the simulated HTTP requests take longer than the time between emissions, only the result of the latest input ('abc') will be outputted, because `switchMap` will cancel the previous requests when a new input comes in.

The `SwitchMap` operator is available in various reactive programming libraries like RxJS (JavaScript), RxJava (Java), RxSwift (Swift), and others. The exact syntax and usage may vary slightly depending on the library, but the core concept remains the same.