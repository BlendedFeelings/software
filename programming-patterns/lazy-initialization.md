---
b: https://blendedfeelings.com/software/programming-patterns/lazy-initialization.md
---

# Lazy Initialization
is a design pattern that defers the creation of an object until the first time it is needed. This can be particularly useful when the instantiation of an object is resource-intensive, and there is a possibility that the object might not be used at all. By using lazy initialization, system resources and processing time can be conserved by delaying the object's creation until it is actually required.

In software development, lazy initialization can be implemented in various ways, but the core concept revolves around a check that occurs when an object is requested. If the object does not yet exist, it is created at that point and stored for future use. If the object has already been created, the stored instance is returned.

Here are some benefits of using lazy initialization:

Reduced application startup time, as less work is done during initialization.
Reduced memory usage if the objects are large or numerous and only a few of them end up being used.
Possibility of avoiding unnecessary computation for objects that are never used.
However, lazy initialization also has some potential drawbacks:

If not implemented carefully, it can lead to issues with thread safety in multi-threaded environments.
It may introduce additional complexity in the code, especially if the initialization involves error handling or resource management.
The first access to the resource might incur a noticeable delay, as the resource is being created on-demand.

```java
class MyClass {
  private MyExpensiveObject myExpensiveObject = null;
  
  public MyExpensiveObject getMyExpensiveObject() {
    if (myExpensiveObject == null) {
      myExpensiveObject = new MyExpensiveObject();
    }
    return myExpensiveObject;
  }
}

```