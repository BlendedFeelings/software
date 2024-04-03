---
b: https://blendedfeelings.com/software/domain-driven-design/value-object.md
---

# Value Objects 
are one of the building blocks of the domain model, alongside Entities. Value Objects are small, simple objects that represent descriptive aspects of the domain with no conceptual identity. They are defined solely by their attributes and are immutable, meaning once they are created, their state cannot be altered.

### Characteristics of Value Objects:

1. **Immutability**: Once created, a Value Object's state cannot change. Any operation that would result in a change must return a new Value Object with the new state.

2. **Equality by Value**: Value Objects are equal to each other when all their fields are equal. Unlike Entities, which are distinguished by a unique identity, Value Objects are compared based on their attribute values.

3. **No Side Effects**: Operations on Value Objects should not have side effects. They can perform calculations or transformations but should not alter the state of other objects.

4. **Self-contained**: A Value Object should be completely self-contained and represent a concept from the domain within its context.

5. **Replaceability**: Value Objects can be freely replaced with other instances of the same Value Object if they have the same value.

6. **Side-Effect-Free Functions**: Functions or methods applied to Value Objects should not produce side effects, either within the Value Object or within the larger domain.

### Examples of Value Objects:

- A `Money` object in a financial application, which encapsulates the amount and currency.
- An `Address` object in a customer management system, which includes street, city, postal code, and country.
- A `DateRange` object in a booking system, which represents a start date and an end date.

### How to Implement Value Objects:

In code, a Value Object is typically implemented as a class with read-only properties and no identity field. Here is an example in C#:

```csharp
public class Address
{
    public string Street { get; }
    public string City { get; }
    public string PostalCode { get; }
    public string Country { get; }

    public Address(string street, string city, string postalCode, string country)
    {
        Street = street;
        City = city;
        PostalCode = postalCode;
        Country = country;
    }

    public override bool Equals(object obj)
    {
        if (obj == null || obj.GetType() != GetType())
            return false;

        Address other = (Address)obj;
        return Street == other.Street &&
               City == other.City &&
               PostalCode == other.PostalCode &&
               Country == other.Country;
    }

    public override int GetHashCode()
    {
        return HashCode.Combine(Street, City, PostalCode, Country);
    }
}
```

### Considerations When Working with Value Objects:

- **Defensive Copying**: When passing a Value Object to another class, provide a copy to prevent the original from being altered if the class is not designed to be immutable.
- **Validation**: Ensure that the Value Object is always in a valid state by validating input data in the constructor or factory methods.
- **Use When Appropriate**: Not all concepts in a domain are best represented as Value Objects. Use Value Objects for concepts that do not require a distinct identity and are immutable.

Value Objects are crucial for creating a rich and expressive domain model that enforces business rules and reduces complexity. They help ensure that domain concepts are properly encapsulated and can lead to more maintainable and understandable code.