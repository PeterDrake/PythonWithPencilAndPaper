# Files
For each page, there is:
* a .py file with the code in question, and
* a .md file with the explanation of the syntax or concepts.

Two programs convert this into human-readable output:
* One produces markdown (and thence pdf) of three pages: the questions (with room for written answers), the explanation, and the answers.
* Another produces an interactive, text-only quizzing program, suitable for use with a screen reader.

These programs should also be able to produce the entire book given the list of topics.

# Question Types
* Evaluate an expression.
* Write code (or fill in a blank in code) to produce (or print) a value.
* Show what a program prints.
* Draw a diagram.
* Write code (or fill in a blank in code) to produce a data structure matching a diagram.

# Special Values
For "evaluate" questions, at least three special situations about what the REPL prints need to be handled:
* The value is `None`. The REPL prints nothing.
* The value is a string. The REPL prints the string, not the repr of that string.
* The expression throws an error.
