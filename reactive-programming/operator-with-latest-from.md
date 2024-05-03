---
b: https://blendedfeelings.com/software/reactive-programming/operator-with-latest-from.md
---

# Operator withLatestFrom  
takes the latest value from the secondary stream(s) and combines it with the value from the primary stream to produce a new value. This is useful for cases where you want to perform calculations or operations that require the latest state from other streams whenever the primary stream updates.

Here's a conceptual example in pseudocode to illustrate how `withLatestFrom` works:

```javascript
// Assume we have a primary stream of button clicks and two secondary streams of data
let buttonClicks = ...; // Stream of button click events
let stream1 = ...; // Stream of data from source 1
let stream2 = ...; // Stream of data from source 2

// Use withLatestFrom to combine the latest values from stream1 and stream2
// with each button click event from the buttonClicks stream
let combinedStream = buttonClicks.withLatestFrom(stream1, stream2, (click, data1, data2) => {
    // This function is called whenever the buttonClicks stream emits a value.
    // data1 and data2 are the latest values from stream1 and stream2 at the time of the click.
    return {
        clickEvent: click,
        latestDataFromStream1: data1,
        latestDataFromStream2: data2
    };
});

// Subscribe to the combined stream to get the combined values
combinedStream.subscribe(combinedValue => {
    // Do something with the combined value
});
```

In this example, whenever the `buttonClicks` stream emits a value (such as when a button is clicked), the `withLatestFrom` operator combines that value with the latest values from `stream1` and `stream2`. The result is then emitted by the `combinedStream`.

It's important to note that `withLatestFrom` will only emit a value when the primary stream emits. If the secondary streams emit values but the primary stream does not, `withLatestFrom` will not produce a new value. Only the latest values from the secondary streams at the time of the primary stream's emission are used.