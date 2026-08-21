# Sets
A *set* is a collection of items, delimited by curly braces `{` and `}`. It is very similar to a list, except that:
* A set cannot contain duplicate items.
* The order of the items in a set does not matter. Two sets are equal if they contain the exactly same elements.

Sets of very small integers tend to be shown in increasing order, but in general the display order is unpredictable and should not be relied on. This is a result of fancy data structures Python uses behind the scenes to make set operations efficient.

A set can be created explicitly using curly braces or using the `set` function. Calling `set` with no argument returns the empty set, displayed as `set()`.

As with strings and lists, the `in` operator can be used to check if something is in a set. `len` returns the size of a set.

The set methods `add` and `remove` modify the set on which they are called, adding or removing an item.

The `&` operator finds the *intersection* of two sets: the set containing only elements that are in both sets.

The `|` operator finds the *union* of two sets: the set containing all elements that are in at least one of the sets.