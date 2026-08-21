# Dictionaries
A *dictionary* (of type `dict`) stores a set of *keys* and associated *values*. The analogy is to a dictionary for a natural human language, in which the keys are words and the values are their definitions.

Each key and its value are separated by a colon. The entire dictionary is delimited by curly braces `{` and `}`.

Pairs can be looked up or replaced using square brackets, as with a list. With a dict, the square brackets contain the key in question rather than an index.

The `in` operator indicates if a given key is present. `len` returns the size of the dict.

To remove a pair from a dict, use the `del` operator:

<pre>del <i>dictonary</i>[<i>key</i>]</pre>

`[]` is obviously the empty list. `{}` is an empty dict. The empty set is represented as `set()`.

The keys of a dictionary can be iterated through using a list comprehension.
