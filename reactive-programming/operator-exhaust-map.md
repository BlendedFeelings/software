---
b: https://blendedfeelings.com/software/reactive-programming/operator-exhaust-map.md
---

# Operator exhaustMap
is a higher-order mapping operator that projects each source value to an Observable which is merged in the output Observable only if the previous projected Observable has completed.

Here's how the `exhaustMap` operator works:

- When a new value arrives from the source Observable, `exhaustMap` calls a provided function with that value, which returns an inner Observable.
- If there is no ongoing inner Observable (i.e., a previous inner Observable has completed), the new inner Observable is subscribed to and its values are emitted to the output Observable.
- If there is an ongoing inner Observable (i.e., a previous inner Observable has not yet completed), the new value from the source is ignored, and no new inner Observable is created.
- Once the current inner Observable completes, `exhaustMap` will accept the next value from the source Observable, creating a new inner Observable.

This behavior is useful in scenarios where you want to ignore new values while processing a current value. It's often used to handle scenarios such as preventing multiple simultaneous API calls triggered by user actions, where only the first call should be executed and the rest should be ignored until the first one completes.

Here is a simple example of how `exhaustMap` might be used in RxJS:

```javascript
import { fromEvent } from 'rxjs';
import { exhaustMap } from 'rxjs/operators';

// Simulate an HTTP request
function simulateHttpRequest(value) {
  return new Observable(observer => {
    setTimeout(() => {
      observer.next(`Completed request with value: ${value}`);
      observer.complete();
    }, 1000); // simulate 1 second HTTP request
  });
}

// Stream of button clicks
const buttonClicks = fromEvent(document.querySelector('button'), 'click');

// Handle button clicks, but ignore new clicks if there is an ongoing request
const httpRequests = buttonClicks.pipe(
  exhaustMap(event => simulateHttpRequest(event.target.value))
);

// Subscribe to the output Observable to see the result
httpRequests.subscribe(data => console.log(data));
```

In this example, if the user clicks the button multiple times in quick succession, only the Observable created from the first click will be executed and subsequent clicks will be ignored until the first Observable completes.