# Variables
A *variable* is a name for something. It can be *assigned* a value with the `=` operator. For example, `x = 3` makes `x` a name for the number 3.

Once it has been assigned a value, the variable can be used in place of the value.

A variable can be redefined by assigning it a new value.

Note that `=` is not a declaration that two things are the same. It is an assignment that makes the variable name on the left a name for the value on the right.

Assignment makes the variable stand for the *value* on the right side, not the code that produced that value. Specifically:
* If a variable is defined in terms of another variable, later changes to the other variable don't affect the first one.
* A variable can be defined in terms of its current value. For example, `x = x + 1` gets the current value of `x`, adds 1, and makes `x` a name for that new value.
