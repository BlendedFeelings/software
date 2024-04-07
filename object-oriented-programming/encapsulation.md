---
b: https://blendedfeelings.com/software/object-oriented-programming/encapsulation.md
---

# Encapsulation 
is one of the fundamental principles of object-oriented programming (OOP). It refers to the bundling of data, along with the methods that operate on that data, into a single unit or class. Additionally, encapsulation is about controlling access to the internal state of an object to protect the integrity of that state.

Here are the key aspects of encapsulation:

1. **Data Hiding**: Encapsulation allows the internal state of an object to be hidden from the outside. This is usually achieved by making the fields (class variables) private and providing public methods to access and modify them. This prevents external entities from directly changing the state.

2. **Accessors and Mutators**: These are methods that get (accessors, also known as getters) and set (mutators, also known as setters) the values of private fields. They provide a controlled way to access and modify the data.

3. **Control over Data**: By encapsulating the data, a class can enforce invariants and constraints on the data. For example, it can prevent negative values where only positive numbers are valid.

4. **Reducing Complexity**: Encapsulation helps in separating the interface from the implementation. Users of a class do not need to understand the complex inner workings of the class to use it.

5. **Maintenance**: Since the implementation details are hidden, changes can often be made to the encapsulated code without affecting other parts of the program.

Here's a simple example in C# that demonstrates encapsulation:

```csharp
public class Account
{
    // Private field: encapsulated data
    private decimal balance;

    // Constructor
    public Account(decimal initialBalance)
    {
        // Validate initial balance
        if (initialBalance < 0)
        {
            throw new ArgumentException("Initial balance cannot be negative.");
        }
        balance = initialBalance;
    }

    // Public method to deposit money: interface to interact with the encapsulated balance
    public void Deposit(decimal amount)
    {
        if (amount <= 0)
        {
            throw new ArgumentException("Deposit amount must be positive.");
        }
        balance += amount;
    }

    // Public method to withdraw money
    public void Withdraw(decimal amount)
    {
        if (amount <= 0)
        {
            throw new ArgumentException("Withdrawal amount must be positive.");
        }
        if (amount > balance)
        {
            throw new InvalidOperationException("Insufficient funds.");
        }
        balance -= amount;
    }

    // Accessor (getter) for the balance
    public decimal GetBalance()
    {
        return balance;
    }
}

class Program
{
    static void Main()
    {
        Account savingsAccount = new Account(1000);  // Create an account with an initial balance
        savingsAccount.Deposit(500);                // Deposit money
        savingsAccount.Withdraw(200);               // Withdraw money
        Console.WriteLine($"The balance is: {savingsAccount.GetBalance()}");  // Output: The balance is: 1300
    }
}
```

In this example, the `Account` class encapsulates the `balance` field by making it private. It provides public methods `Deposit`, `Withdraw`, and `GetBalance` to interact with the balance in a controlled manner. This ensures that the balance cannot be set to an invalid state from outside the class.