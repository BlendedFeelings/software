---
b: https://blendedfeelings.com/software/reactive-programming/concatenating-streams.md
---

# Concatenating streams means 
that you want to create a new stream that emits all the items from the first stream and then, once the first stream completes, it starts emitting items from the second stream, and so on if there are more streams involved.

Here's how you can concatenate streams in different reactive programming libraries:

### RxJS (JavaScript)

In RxJS, you can use the `concat` operator to concatenate multiple observables:

```javascript
import { concat, of } from 'rxjs';

const stream1 = of(1, 2, 3);
const stream2 = of(4, 5, 6);
const concatenatedStream = concat(stream1, stream2);

concatenatedStream.subscribe(value => console.log(value));
// Output will be: 1 2 3 4 5 6
```

When concatenating streams, it's important to remember that the second stream will not start until the first one has completed. If any stream does not complete, subsequent streams will not be subscribed to and their values will not be emitted.