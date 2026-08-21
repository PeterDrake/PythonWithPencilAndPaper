# If Statements
An `if` statement executes one or more statements if and only if some condition is true. The general form is:

<pre>
if <i>condition</i>:
    <i>statement(s)</i>
</pre>

An optional `else` clause provides alternate statements to be executed if the condition is *not* true:

<pre>
if <i>condition</i>:
    <i>statement(s)</i>
else:
    <i>statement(s)</i>
</pre>

Even more conditions can be provided by including `elif` (short for "else if") clauses:

<pre>
if <i>condition1</i>:
    <i>statement(s)</i>
elif <i>condition2</i>:
    <i>statement(s)</i>
else:
    <i>statement(s)</i>
</pre>

The statement stops after the first true condition.
