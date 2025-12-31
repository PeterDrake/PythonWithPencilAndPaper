<style> table th:nth-of-type(1) { width: 10%; } table th:nth-of-type(2) { width: 45%; } table th:nth-of-type(3) { width: 45%; } </style>
|Number|Expression|Value|
|---|---|---|
|1|`2 + 2`|`4`|
|2|`2 + 3`|| |
|3|`4 - 1`|| |
|4|`3 - 8`|| |
|5|`2 * 4`|| |
|6|`8 / 2`|| |
|7|`7 / 2`|| |
|8|`7 // 2`|| |
|9|`34 // 10`|| |
|10|`34 % 10`|| |
|11|`2 ** 3`|| |
|12|`10 ** 20`|| |
|13|`2 + 3 * 5`|| |
|14|`2 + (3 * 5)`|| |
|15|`(2 + 3) * 5`|| |
|16|`1 + 2 * 3 - 4 ** 2 / 4`|| |
# Arithmetic Operators
Numbers can be combined with familiar arithmetic operators. `+` and `-` perform addition and subtraction. The multiplication operator is `*`.

There are three division operators:
* `/` performs standard division. The answer always includes a decimal point, even if it happens to be an integer.
* `//` performs integer division, throwing away any remainder.
* `%`, the *modulo* or *remainder* operator, keeps *only* the remainder.

The `**` operator performs exponentiation, so `5 ** 2` computes $5^2$.

Some operators have higher precedence than others, so they are performed first:
* `**` has the highest precedence
* `*`, `/`, `//`, and `%` have the next highest
* `+` and `-` have the lowest

Parentheses can be used to ensure that particular operations are performed earlier.

|Number|Expression|Value|
|---|---|---|
|1|`2 + 2`|`4`|
|2|`2 + 3`|`5`|
|3|`4 - 1`|`3`|
|4|`3 - 8`|`-5`|
|5|`2 * 4`|`8`|
|6|`8 / 2`|`4.0`|
|7|`7 / 2`|`3.5`|
|8|`7 // 2`|`3`|
|9|`34 // 10`|`3`|
|10|`34 % 10`|`4`|
|11|`2 ** 3`|`8`|
|12|`10 ** 20`|`100000000000000000000`|
|13|`2 + 3 * 5`|`17`|
|14|`2 + (3 * 5)`|`17`|
|15|`(2 + 3) * 5`|`25`|
|16|`1 + 2 * 3 - 4 ** 2 / 4`|`3.0`|
