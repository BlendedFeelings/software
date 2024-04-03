---
b: https://blendedfeelings.com/software/programming-patterns/builder-pattern.md
---

# Builder Pattern
is a design pattern that is used to construct a complex object step by step. The Builder pattern allows for the creation of different representations of a complex object by separating the construction process from the representation itself.

The primary intent of the Builder pattern is to:

Separate the construction of a complex object from its representation so that the same construction process can create different representations.
Allow for fine control over the construction process.
The pattern is particularly useful when an object needs to be created with many possible configurations, and it's not practical to have constructors for every possible combination of parameters.

```csharp
public class Product
{
    public string PartA { get; private set; }
    public string PartB { get; private set; }
    public string PartC { get; private set; }

    public class Builder
    {
        private readonly Product _product = new Product();

        public Builder SetPartA(string partA)
        {
            _product.PartA = partA;
            return this;
        }

        public Builder SetPartB(string partB)
        {
            _product.PartB = partB;
            return this;
        }

        public Builder SetPartC(string partC)
        {
            _product.PartC = partC;
            return this;
        }

        public Product Build()
        {
            return _product;
        }
    }
}

// Usage
Product product = new Product.Builder()
    .SetPartA("Data for Part A")
    .SetPartB("Data for Part B")
    .SetPartC("Data for Part C")
    .Build();
```