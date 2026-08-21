# While Loops
A `while` loop allows one or more statements to be executed repeatedly. The general form is:

<pre>
while <i>condition</i>:
    <i>statement(s)</i>
</pre>

The condition is checked at the beginning of each pass through the loop. If it is true, the statements are executed. The condition is then checked again, and so on.

The condition is only checked at the beginning of each pass through the loop. The loop does not end mid-pass merely because the condition has become false.

A `while` loop can replicate what a list comprehension does, but the list comprehension is more convenient for this specific task.