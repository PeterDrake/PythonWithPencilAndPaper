# F-Strings
If a string is preceded by `f` (just outside the quotation marks), anything within curly braces `{}` inside that string is evaluated rather than taken as literal text.

A number of specifications can be provided, inside the curly braces after a colon `:`, for how the resulting value should be formatted. Specifically:

* '.' and a number specifies the maximum number of digits to show after the decimal point.
* '<' and a number adds spaces to pad the representation to the specified total length. The value is therefore left justified, which can be handy when printing tables.
* `>` and a number similarly adds spaces, but at the beginning, giving right justification.
