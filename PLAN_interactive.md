# Plan for `src/interactive.py`

## Overview
A terminal-based interactive quiz that mirrors the PDF's structure, designed for screen reader/Braille compatibility (plain text, no ANSI codes, clear section breaks).

## Data Model

Each exercise is parsed from a `.py` file (same as `generate_pdf.py`):
- Lines are grouped by blank lines
- Each group = one exercise
- All lines except the last are **statements** (executed for context but not answered)
- The last line is the **expression** to evaluate

A `dict` per exercise:
```python
{
    "number": int,
    "statements": list[str],   # e.g. ["x = 3", "y = 4"]
    "expression": str,         # e.g. "x + y"
    "answer": str,             # repr(eval(...))
}
```

## Flow (per topic)

1. **Phase 1 — Initial attempt**: For each exercise, print the number, any statements, and the expression. Prompt for input. Store the answer.
2. **Phase 2 — Explanation**: Print the content of the corresponding markdown file (minus HTML/script tags).
3. **Phase 3 — Review**: For each exercise, reprint the prompt and the user's previous answer. Ask if they want to keep it (Enter) or type a new one.
4. **Phase 4 — Results**: For each exercise, print the prompt, the correct answer, and the user's answer if wrong.

## Program structure

```
main()
  - Read topics list from text/topics.txt
  - For each topic:
      - Parse exercises from src/{topic}.py
      - Run the 4-phase quiz loop
      - Print a topic separator
  - Print final summary (score per topic)

parse_exercises(filepath) -> list[Exercise]
  - Same grouping logic as generate_pdf.py

load_explanation(topic) -> str
  - Read text/{topic}.md, strip HTML/script tags

run_quiz(topic, exercises, explanation)
  - Implements the 4 phases above
```

## Key design decisions
- **Plain text only** — no color, no cursor manipulation, works with screen readers
- **`input()` prompts** with clear labels like `Exercise 1:` and `Your answer:`
- **Answers compared as strings** after `repr()` of the correct result (matching `generate_pdf.py`'s approach)
- **Blank lines** between sections for readable screen reader output
- Topics read from `text/topics.txt` rather than hardcoded
