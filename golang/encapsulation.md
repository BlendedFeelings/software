---
b: https://blendedfeelings.com/software/golang/encapsulation.md
---

# Encapsulation In Go 
which is not a pure object-oriented programming language, is achieved through the use of packages and visibility rules. Go does not have classes; instead, it has types with methods associated with them.

Here's how encapsulation works in Go:

1. **Package Scope**: Identifiers (names of types, functions, variables, etc.) that start with an uppercase letter are exported (visible and accessible outside the package), while identifiers that start with a lowercase letter are unexported (only visible within the package).

2. **Structs and Methods**: In Go, you create a struct to hold your data and then define methods on that struct. By convention, you only export fields and methods that should be accessible outside the package.

Here's an example of encapsulation in Go:

```go
package bank

// Account is an example of an encapsulated structure.
// Only the exported fields can be directly accessed from outside the package.
type Account struct {
    Owner   string  // Exported - accessible outside the package
    balance float64 // Unexported - not accessible outside the package
}

// NewAccount is a constructor function to create a new Account.
// It is exported because it starts with an uppercase letter.
func NewAccount(owner string) *Account {
    return &Account{Owner: owner, balance: 0.0}
}

// Deposit is an exported method that allows adding funds to the account.
func (a *Account) Deposit(amount float64) {
    if amount > 0 {
        a.balance += amount
    }
}

// Balance is an exported method that allows fetching the account balance.
// It does not allow direct access to the balance field, providing encapsulation.
func (a *Account) Balance() float64 {
    return a.balance
}

// withdraw is an unexported method, it's only accessible within the bank package.
func (a *Account) withdraw(amount float64) bool {
    if amount > 0 && amount <= a.balance {
        a.balance -= amount
        return true
    }
    return false
}
```

In this example, the `Account` struct has one exported field (`Owner`) and one unexported field (`balance`). The `NewAccount` function is exported and can be used to create new `Account` instances. The `Deposit` and `Balance` methods are exported, allowing interaction with the account's balance without providing direct access to the balance field. The `withdraw` method is unexported and can only be called within the `bank` package.

By following these conventions, you can encapsulate the internal state of your types and expose only what's necessary, ensuring that the internal representation of the object is hidden from the outside.