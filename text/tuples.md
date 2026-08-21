# Tuples
A *tuple* is almost exactly the same as a list, but it is delimited by round parentheses `(` and `)`. The difference is that a tuple, unlike a list, is *immutable*: it cannot be modified. This is helpful for a couple of reasons:
* The same tuple can have several names without any risk of the aliasing problems described previously under Equality.
* Because of the underlying efficient data structures, set elements and dictionary keys have to be immutable. Tuples work for this but lists don't.

Several variables can be assigned to the elements of a tuple with one assignment statement. The tuple is said to be *unpacked*. Conversely, if several values (separated by commas) appear on the right side of an assignment statement, they are *packed* into a tuple.

A tuple with exactly one element has a comma after that element. Otherwise, something like `(2)` would be ambiguous.
