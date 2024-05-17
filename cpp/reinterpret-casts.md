---
b: https://blendedfeelings.com/software/cpp/reinterpret-casts.md
---

# Operator `reinterpret_cast` 
is a type of casting operator in C++. It is used to convert one pointer type to another pointer type, even if the types are unrelated. This cast can also be used to cast from a pointer to an integral type and vice versa. It is a very powerful casting operator that does not check if the pointer type and the data pointed to are compatible, which can lead to unsafe code if not used carefully.

Here's how you use `reinterpret_cast`:

```cpp
TypeA *a = new TypeA;
TypeB *b = reinterpret_cast<TypeB*>(a);
```

In this example, `a` is a pointer to an object of `TypeA`, and `b` is a pointer to `TypeB`. The `reinterpret_cast` converts the pointer `a` to the type `TypeB*`. This does not change the actual object or its memory layout; it simply tells the compiler to treat the memory at that address as if it were a `TypeB` object.

It's important to be cautious when using `reinterpret_cast` because it can lead to undefined behavior if the cast is invalid. For example, if `TypeA` and `TypeB` have different memory layouts and you try to use `b` to access the object's members, you might access the wrong memory, which can cause your program to crash or behave incorrectly.

`reinterpret_cast` is often used in low-level programming, such as interfacing with hardware, working with memory-mapped input/output, or when converting function pointers. However, it should be avoided in high-level code unless absolutely necessary, as it can break the type safety that C++ provides.

Here are some guidelines when using `reinterpret_cast`:

- Use it only when you know exactly what you are doing and understand the potential risks.
- Prefer safer casts like `static_cast` or `dynamic_cast` when possible.
- Keep the use of `reinterpret_cast` localized and well-documented to make your code easier to maintain and understand.
- Ensure that any assumptions you make about the size and layout of objects are verified and portable across different platforms and compilers.