# Comparisons
There are several operators for comparing things:

* `<` less than  
* `<=` less than or equal to  
* `==` equal  
* `>=` greater than or equal to  
* `>` greater than  
* `!=` not equal to  

The resulting value is either `True` or `False`.

Note the difference between `a = 1`, which means "Make `a` a name for 1.", and `a == 1`, which means "Is `a` equal to 1?".

When comparing sequences like strings and lists, comparisons examine the first element of each. If they are equal, the comparison proceeds to the next element. If a difference is found, or one sequence runs out first, the sequences are not equal.

Characters are compared according to the Unicode specification. Digits are less than upper-case letters, which are in turn less than lower-case letters. Within these groups, smaller digits and earlier letters in the alphabet are considered less.