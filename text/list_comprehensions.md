# List Comprehensions
A *list comprehension* is a way of converting a list (or other sequence) into another list. The general form is:

<pre>[<i>expr</i> for <i>var</i> in <i>sequence</i>]</pre>

The value of this is found by assigning `var` to each element of `sequence` in turn, then evaluating `expr` (an expression which may involve `var`).

Optionally, a list comprehension can also include a condition:

<pre>[<i>expr</i> for <i>var</i> in <i>sequence</i> if <i>condition</i>]</pre>

Elements for which this condition is false are omitted from the result.
