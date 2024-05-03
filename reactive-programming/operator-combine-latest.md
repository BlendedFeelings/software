---
b: https://blendedfeelings.com/software/reactive-programming/operator-combine-latest.md
---

# Operator combineLatest
is used to combine multiple observable streams into a single observable stream by taking the latest values from each of the combined streams whenever any of them emits a new value.

Here's how `combineLatest` works:

1. You pass multiple observables to `combineLatest`.
2. It waits until all the observables have emitted at least one value.
3. Once all observables have emitted an initial value, `combineLatest` emits a combined value as an array containing the latest values from each observable.
4. After the initial emission, any time one of the observables emits a new value, `combineLatest` will emit a new array containing the latest values from all observables.
5. The resulting observable will only complete when all of the combined observables complete. If any of the observables errors out, the resulting observable will error out as well.

Here's an example in JavaScript using RxJS:

```javascript
import { combineLatest } from 'rxjs';

// Create some observables
const observable1 = of(1, 2, 3);
const observable2 = of('a', 'b', 'c');

// Use combineLatest
const combined = combineLatest([observable1, observable2]);

combined.subscribe(value => {
  console.log(value);
});

// Output will be:
// [3, 'a'] - when observable2 emits 'a' (observable1 has completed with '3')
// [3, 'b'] - when observable2 emits 'b'
// [3, 'c'] - when observable2 emits 'c'
```

In this example, `observable1` completes quickly (since it's just emitting 1, 2, 3 in sequence), but `combineLatest` will wait until `observable2` starts emitting values. The output is the latest values from both observables, which in this case will be '3' from `observable1` and the latest letter from `observable2`.

`combineLatest` is particularly useful when you have multiple streams of data that you want to combine and use together, for instance, when you need to calculate a value that depends on the latest values from several streams.