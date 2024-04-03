---
b: https://blendedfeelings.com/software/programming-patterns/object-pool-pattern.md
---

# Object Pool pattern
is a software design pattern that is used to manage the reuse of objects in an application. It is particularly useful in situations where the cost of initializing a class instance is high, the rate of instantiation of a class is high, and the number of instances in use at any one time is low. The Object Pool pattern can improve performance and memory use by reusing objects from a fixed pool instead of allocating and freeing them individually.

Here's how the Object Pool pattern works:

**Object Pool Creation**: An object pool is created to manage a set of instances of a particular class.

**Acquire Object**: When a client requests an object, the pool checks if there are any available instances. If so, it returns an existing instance from the pool.

**Release Object**: After the client has finished using the object, the object is returned to the pool rather than being destroyed. This way, it can be reused by another client.

**Pool Management**: The pool may have methods to manage the pool size, such as expanding the pool (creating new instances) if necessary or shrinking it by destroying instances that are not frequently used.

```java
class Object {
    // Define your object here
}

// Define the object pool
class ObjectPool {
    private objects: Object[];

    borrowObject(): T {
        var obj: Object;
        if (this.objects.length > 0) {
            obj = this.objects.pop();
        } else {
            obj = this.create();
        }

        if (!this.validate(obj)) {
            this.destroy(obj);
            obj = this.borrowObject();
        }

        return obj;
    }

    returnObject(obj: T) {
        if (this.validate(obj)) {
            this.objects.push(obj);
        } else {
            this.destroy(obj);
        }
    }
}

// Usage
var pool = new ObjectPool();
var obj1 = pool.borrowObject();
var obj2 = pool.borrowObject();
pool.returnObject(obj1);
pool.returnObject(obj2);

```