---
b: https://blendedfeelings.com/software/python/class-encapsulation.md
---

# Ecapsulation in Python
is the concept of bundling data (variables) and methods (functions) that work on the data into a single unit, or class. Encapsulation also involves restricting access to the inner workings of that class, which is known as information hiding. This is typically achieved by using private and protected access modifiers. However, Python does not have the strict access control mechanisms found in languages like Java or C++. Instead, it relies on naming conventions and some property mechanisms to achieve a similar effect.

Here's an example of a simple class in Python that uses encapsulation:

```python
class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number  # Protected attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            raise ValueError("Balance cannot be negative.")

    balance = property(get_balance, set_balance)

account = BankAccount('12345678', 100)
account.deposit(50)
print(account.balance)  # Output: 150
account.withdraw(20)
print(account.balance)  # Output: 130
```

In this example:

- The `__init__` method is the constructor and is used to initialize the object's attributes.
- The `_account_number` attribute is meant to be protected, which is indicated by a single underscore. This is a convention to tell other programmers that this attribute should be treated as a non-public part of the API.
- The `__balance` attribute is meant to be private, which is indicated by the double underscore. This triggers name mangling, making it harder to access from outside the class.
- The `deposit` and `withdraw` methods are public methods that allow interaction with the private `__balance` attribute.
- The `get_balance` and `set_balance` methods are used to safely access and modify the private `__balance` attribute. They are used to create a property named `balance`, which allows controlled access to the private `__balance` attribute from outside the class.

Remember that in Python, "private" and "protected" attributes are largely based on convention and are not enforced by the language itself. The single and double underscores are just naming conventions that signal the intended level of privacy for class members. The double underscore triggers name mangling to make it harder (but not impossible) to access the attribute from outside the class.