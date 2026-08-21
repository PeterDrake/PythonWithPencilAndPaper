# Defining Functions
In addition to the many functions built into Python, you can define your own. The general format is

<pre>
def <i>name</i>(<i>parameter(s)</i>):
    <i>statement(s)</i>
</pre>

where zero or more parameters are separated by commas and one or more statements are on successive lines.

Carefully note the colon `:` at the end of the first line and the indentation of the statements within the definition.

When the function is called, the parameters are assigned as names for whatever values are passed in as arguments. The statements are then executed in order.

If the function reaches a `return` statement, the value specified is returned as the value of the function call.

The parameters of a function are only visible inside that function. There are several subtleties to this:
* Even if a parameter happens to have the same name as a global variable, setting it inside the function does not affect the global variable. It is said to *shadow* the global variable, which is no longer visible inside the function.
* Assigning a value inside a function creates a new *local variable*, which shadows any global variable with the same name.
* Unshadowed global variables can be *read* inside a function.
* If a parameter or local variable names a mutable object (like a list), modifying that object does affect other names for it outside the function.