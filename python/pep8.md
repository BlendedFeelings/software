---
b: https://blendedfeelings.com/software/python/pep8.md
---

# PEP 8 is 
the Style Guide for Python Code, which provides a set of rules and guidelines on how to format Python code for maximum readability. Here are some key points from PEP 8:

### Indentation
- Use 4 spaces per indentation level.
- Continued lines should align wrapped elements either vertically using Python's implicit line joining inside parentheses, brackets, and braces, or using a hanging indent.

### Tabs or Spaces
- Spaces are the preferred indentation method.
- Tabs should be used solely to remain consistent with code that is already indented with tabs.

### Maximum Line Length
- Limit all lines to a maximum of 79 characters for code and 72 for comments and docstrings.

### Blank Lines
- Surround top-level function and class definitions with two blank lines.
- Method definitions inside a class are surrounded by a single blank line.
- Extra blank lines may be used (sparingly) to separate groups of related functions.

### Imports
- Imports should usually be on separate lines.
- Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.

### Whitespace in Expressions and Statements
- Avoid extraneous whitespace in the following situations:
  - Immediately inside parentheses, brackets, or braces.
  - Immediately before a comma, semicolon, or colon.
  - Immediately before the open parenthesis that starts the argument list of a function call.
  - Immediately before the open parenthesis that starts an indexing or slicing.
  - More than one space around an assignment (or other) operator to align it with another.

### Comments
- Comments should be complete sentences.
- If a comment is short, the period at the end can be omitted.
- Block comments generally consist of one or more paragraphs built out of complete sentences, with each sentence ending in a period.

### Naming Conventions
- Function names should be lowercase, with words separated by underscores as necessary to improve readability.
- Variable names follow the same convention as function names.
- Constants are usually defined on a module level and written in all capital letters with underscores separating words.
- Class names should normally use the CapWords convention.

### Programming Recommendations
- Code should be written in a way that does not disadvantage other implementations of Python (PyPy, Jython, IronPython, Cython, Psyco, and such).
- Don’t compare boolean values to True or False using `==`.
- Function annotations should use the normal rules for colons and always have spaces around the `->` if present.

This is just a summary. For the full guide, you should refer to the official PEP 8 document, which can be found at: https://www.python.org/dev/peps/pep-0008/