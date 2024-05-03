---
b: https://blendedfeelings.com/software/concepts/command-query-separation.md
---

# Command-query separation (CQS) 
is a principle of software design proposed by Bertrand Meyer, which states that every method in an object should either be a command that performs an action or a query that returns data to the caller, but not both. In other words, a command changes the state of an object but does not return any data, whereas a query returns data but does not change the state.

### Commands:
- Perform an action.
- Change the state of an object or system.
- Do not return any data (or if they do, it is only status information about the action performed, such as success or failure).
- Examples: `void SaveRecord(Record record)`, `void DeleteUser(int userId)`

### Queries:
- Return data.
- Do not change the state of an object or system.
- Have no side effects.
- Examples: `Record GetRecordById(int id)`, `int GetUserCount()`

### Benefits of CQS:
- **Clarity**: It's clear whether a method changes the state or just retrieves data.
- **Maintainability**: Separating commands and queries can lead to more maintainable code since it's easier to reason about the effects of methods.
- **Reduced Side Effects**: By segregating methods that mutate state from those that don't, the potential for unexpected side effects is reduced.
- **Easier Debugging**: When a method only performs one action, it's easier to track down bugs related to state changes or data retrieval.

### Example in C#:
```csharp
public class Account
{
    public decimal Balance { get; private set; }

    // Command: Increases the balance, does not return any data
    public void Deposit(decimal amount)
    {
        if (amount > 0)
        {
            Balance += amount;
        }
    }

    // Query: Returns the balance, does not change the state
    public decimal GetBalance()
    {
        return Balance;
    }
}
```

In this example, `Deposit` is a command because it changes the state of the `Account` by increasing the balance. `GetBalance` is a query because it returns the current balance without changing the state of the `Account`.

CQS is particularly useful in the context of object-oriented programming and can also be applied in other paradigms such as functional programming, where it aligns with the concept of pure functions for queries. However, it's important to note that CQS is not always strictly applicable, and there are scenarios where a method might need to perform an action and return data. In such cases, careful design decisions are required to maintain clarity and maintainability.