---
b: https://blendedfeelings.com/software/python/special-method.md
---

# Special methods in Python
are a set of predefined methods that you can override in your class definitions to customize the behavior of your objects with respect to built-in Python operations. These methods are always surrounded by double underscores (e.g., `__init__`, `__str__`, etc.). They are also known as "magic methods" or "dunder methods" (dunder stands for "double underscore").

Here are some commonly used special methods in Python:

1. `__init__(self, ...)`: The constructor method for a class. Called when an object is created.

2. `__del__(self)`: The destructor method. Called when an object is about to be destroyed.

3. `__str__(self)`: Called by the `str()` built-in function and by the `print` statement to compute the "informal" or nicely printable string representation of an object.

4. `__repr__(self)`: Called by the `repr()` built-in function to compute the "official" string representation of an object. This is often used for debugging.

5. `__len__(self)`: Called to implement the built-in function `len()`. Should return the length of the object, an integer >= 0.

6. `__getitem__(self, key)`: Called to implement evaluation of `self[key]`. Should return the value for the specified key.

7. `__setitem__(self, key, value)`: Called to implement assignment to `self[key]`.

8. `__delitem__(self, key)`: Called to implement deletion of `self[key]`.

9. `__iter__(self)`: Called when an iterator is required for a container.

10. `__next__(self)`: Called to implement the iterator protocol. Should return the next item from the container.

11. `__contains__(self, item)`: Called to implement membership test operators. Should return `True` if `item` is in the object, `False` otherwise.

12. `__eq__(self, other)`: Called to implement evaluation of `self == other`.

13. `__ne__(self, other)`: Called to implement evaluation of `self != other`.

14. `__lt__(self, other)`: Called to implement evaluation of `self < other`.

15. `__le__(self, other)`: Called to implement evaluation of `self <= other`.

16. `__gt__(self, other)`: Called to implement evaluation of `self > other`.

17. `__ge__(self, other)`: Called to implement evaluation of `self >= other`.

18. `__add__(self, other)`: Called to implement addition `self + other`.

19. `__sub__(self, other)`: Called to implement subtraction `self - other`.

20. `__mul__(self, other)`: Called to implement multiplication `self * other`.

21. `__truediv__(self, other)`: Called to implement true division `self / other`.

22. `__floordiv__(self, other)`: Called to implement floor division `self // other`.

23. `__mod__(self, other)`: Called to implement the modulo operation `self % other`.

24. `__pow__(self, other[, modulo])`: Called to implement power operation `self ** other`.

25. `__and__(self, other)`: Called to implement the bitwise AND operation `self & other`.

26. `__or__(self, other)`: Called to implement the bitwise OR operation `self | other`.

27. `__xor__(self, other)`: Called to implement the bitwise XOR operation `self ^ other`.

28. `__lshift__(self, other)`: Called to implement the left bitwise shift operation `self << other`.

29. `__rshift__(self, other)`: Called to implement the right bitwise shift operation `self >> other`.

30. `__invert__(self)`: Called to implement the unary bitwise inversion operation `~self`.

These are just a few examples; there are many more special methods available in Python. By defining these methods in your classes, you can create objects that behave like built-in types, allowing for more idiomatic and Pythonic code.