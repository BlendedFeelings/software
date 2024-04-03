---
b: https://blendedfeelings.com/software/programming-patterns/collection-pipeline-pattern.md
---

# Collection Pipeline
is used to process collections of data by chaining together a series of operations that transform the data. It is often used in functional programming languages. Each operation takes the output of the previous operation as its input, and the result of the last operation is the final output of the pipeline. 

```java
// Data class
class Person {
    private String name;
    private int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    String getName() {
        return name;
    }

    int getAge() {
        return age;
    }
}

// Collection Pipeline
List<Person> people = Arrays.asList(
    new Person("Alice", 25),
    new Person("Bob", 30),
    new Person("Charlie", 35),
    new Person("David", 40)
);

// // Usage, chaining operations
List<String> names = people
    .filter(person -> person.getAge() > 30)
    .map(person -> person.getName())
    .collect();
print(names);
```