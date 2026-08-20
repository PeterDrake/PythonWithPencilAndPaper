# Methods
*Methods* are very similar to functions. Either might return a value or have some side effect like modifying the contents of a list. They are called slightly differently:

* `f(x, y)` is the function `f` being called and given the arguments `x` and `y`. This says to Python, "Hey function `f`, do your thing. You'll need `x` and `y`."
* `x.m(y)` is the method `m` being called *on* the object `x` and given the argument `y`. This says, "Hey object `x`, do `m`. You'll need `y`."

Methods are generally "about" the objects on which they are called.

List methods include:
* `append` modifies the list by adding its argument to the end.
* `extend` modifies the list by adding each element of its argument to the end.
* `insert` inserts an element at a specific index, moving everything after that one position to the right.
* `index` returns the position where the argument first appears in the list.
* `count` returns the number of times the argument appears in the list.
* `remove` removes the first appearance of the argument from the list.
* `sort` modifies the list by sorting it. This is different from the `sorted` function, which creates a new list.

String methods include:
* `split` returns a list of strings found by breaking the string apart. By default, it looks for spaces to break the string into words, but some other separator can be given as an argument.
* `join` creates a string from a list of strings. The string on which the method is called is used as the separator.