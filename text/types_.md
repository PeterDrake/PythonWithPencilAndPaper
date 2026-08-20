# Types
Every value has a *type*. Conversely, each type is the set of values that have that type.

Types we have seen so far include:

`int` Integer  
`float` Number including a decimal point or scientific notation, even if it happens to be an integer  
`str` String  
`list` List  
`bool` Boolean logical value: `True` or `False`

The built-in `type` function returns the type of its argument. For example, `type(20)` returns `<class 'int'>`. This is the `int` type; the reason for the more elaborate notation is beyond the scope of this book.

Each type is also the name of a function for converting values of other types. For example, `int('15')`, having been given the string `'15'`, returns the int `15`.

The type conversion functions generally behave as expected, but:
* Some conversions are not possible. `int('hello')` results in an error.
* Converting a float to an int discards anything after the decimal point.
* `bool` converts any zero or empty value to `False` and any other value to `True`.