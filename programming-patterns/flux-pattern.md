---
b: https://blendedfeelings.com/software/programming-patterns/flux-pattern.md
---

# Flux Pattern
is a design pattern used in software development, particularly in user interfaces, to manage the flow of data and state changes. It involves a unidirectional flow of data, where all changes to the state of an application must go through a central dispatcher.

In simpler terms, Flux pattern helps to ensure that all changes to an application's data are managed in a consistent and controlled way.

Here is an example of how to implement Flux pattern in C#:

First, we define our data store:

```
public class DataStore
{
    private int _counter = 0;

    public event Action<int> CounterChanged;

    public int Counter
    {
        get => _counter;
        set
        {
            _counter = value;
            CounterChanged?.Invoke(_counter);
        }
    }
}
```

Next, we define our actions:

```
public class CounterActions
{
    public static void IncrementCounter(DataStore store)
    {
        store.Counter++;
    }

    public static void DecrementCounter(DataStore store)
    {
        store.Counter--;
    }
}
```

Then, we define our dispatcher:

```
public class Dispatcher
{
    public static void Dispatch(Action action, DataStore store)
    {
        action.Invoke();
    }
}
```

Finally, we use these components together in our application:

```
static void Main(string[] args)
{
    var store = new DataStore();

    store.CounterChanged += count => Console.WriteLine($"Counter changed: {count}");

    Dispatcher.Dispatch(() => CounterActions.IncrementCounter(store), store);
    Dispatcher.Dispatch(() => CounterActions.DecrementCounter(store), store);
}
```

In this example, the data store manages the state of our application (in this case, a simple counter) and notifies any interested parties (in this case, the console) when the state changes. The actions define the possible changes to the state, and the dispatcher ensures that these changes are made in a controlled way.