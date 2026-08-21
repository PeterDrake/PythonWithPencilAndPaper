# Equality
What does it mean for two variables `x` and `y` to be equal? There are two possibilities:
1. `x` and `y` are two names for *the same object*
2. `x` and `y` are names for objects that *have the same content*, whether or not they are the same object

Python's `==` operator uses the second interpretation.

Usually the difference doesn't matter, but for objects than can be modified (like lists, sets, and dictionaries), it does. Specifically, suppose `x` and `y` are *aliases* for the same object. Modifying the object named by `x` also modifies the object named by 'y', because they are the same object.

Assigning `x` to name *a different object* does not modify `y` in this situation.

The `copy` method, provided by lists, sets, and dicts, makes a copy of an object.

