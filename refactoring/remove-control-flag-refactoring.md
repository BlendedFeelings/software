---
b: https://blendedfeelings.com/software/refactoring/remove-control-flag-refactoring.md
---

# Remove Control Flag 
refactoring technique is about simplifying the flow of a program by eliminating variables that are used as flags to control multiple loops or conditional statements. These flags can make the code harder to read and understand because they require the reader to track the flag's state across different parts of the code. Instead, you can use break, continue, or return statements to manage control flow more directly.

Here's a step-by-step guide on how to apply the "Remove Control Flag" refactoring technique:

1. **Identify Control Flag**: Find a variable that is being used as a control flag to determine the flow of execution in loops or conditional statements.

2. **Replace with Break or Continue**: If the control flag is used within a loop to determine when to exit, replace it with a `break` or `continue` statement.

3. **Replace with Return**: If the control flag is used to determine when to exit a method, replace it with a `return` statement.

4. **Remove Control Flag**: Once the control flag is no longer needed to control the flow, remove the variable entirely.

5. **Test**: Run your tests to ensure that the behavior of the program remains unchanged.

Here's an example in C#:

Before refactoring:

```csharp
public void CheckSecurity(string[] people)
{
    bool found = false;
    for (int i = 0; i < people.Length; i++)
    {
        if (!found)
        {
            if (people[i].Equals("Don"))
            {
                SendAlert();
                found = true;
            }
            if (people[i].Equals("John"))
            {
                SendAlert();
                found = true;
            }
        }
    }
}
```

After applying "Remove Control Flag" refactoring:

```csharp
public void CheckSecurity(string[] people)
{
    for (int i = 0; i < people.Length; i++)
    {
        if (people[i].Equals("Don"))
        {
            SendAlert();
            break; // Replaces the control flag with a break statement
        }
        if (people[i].Equals("John"))
        {
            SendAlert();
            break; // Replaces the control flag with a break statement
        }
    }
}
```

In this example, the `found` variable was used as a control flag to prevent further checks once a match was found. By using a `break` statement, we can exit the loop immediately after sending an alert, making the `found` variable unnecessary. This simplifies the code by removing the extra variable and the checks associated with it.