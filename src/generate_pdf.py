from io import StringIO
from markdown_pdf import MarkdownPdf, Section

CSS = 'body {line-height: 2}\n'

def generate_exercises(topic, title, show_answers=False):
    # print(f'TOPIC: {topic}')
    context = {}
    builder = StringIO()  # For efficiency, as we're building a very large string
    if show_answers:
        builder.write(title + ' (Solutions)\n')
    else:
        builder.write(title + ' (Exercises)\n')
    with open(f'{topic}.py') as infile:
        buffer = []  # Each batch of consecutive lines is accumulated here
        n = 1
        while line := infile.readline():
            line = line.rstrip()
            if line == '':
                if buffer:
                    generate_question(n, buffer, builder, context, show_answers)
                    n += 1
                else:
                    print(f'Multiple blank lines in {topic}.py')
                buffer = []
            else:
                buffer.append(line)
        if buffer:  # Generate last question of page, which is not followed by a blank line
            generate_question(n, buffer, builder, context, show_answers)
    result = builder.getvalue()
    builder.close()
    return result

def generate_question(n, lines, builder, context, show_answers):
    if len(lines) > 1:  # There are some preliminary statements before the expression
        # print(f'CONTEXT: {'\n'.join(lines[:-1])}')
        exec('\n'.join(lines[:-1]), context)
        padded_line = pad_with_nonbreaking_spaces(lines[0], 30) + '&nbsp;&nbsp;'
        builder.write(f'{n}. `{padded_line}`  \n')
        for line in lines[1:-1]:
            padded_line = pad_with_nonbreaking_spaces(line, 30) + '&nbsp;&nbsp;'
            builder.write(f'   `{padded_line}`  \n')
    # Now deal with the expression itself
    padded_line = pad_with_nonbreaking_spaces(lines[-1], 30) + '&nbsp;&nbsp;'
    # print(f'EXPRESSION: {lines[-1]}')
    if len(lines) == 1:
        builder.write(f'{n}. `{padded_line}`')
    else:
        builder.write(f'   `{padded_line}`')
    if n == 1 or show_answers:
        builder.write(f'<ins>`{pad_with_nonbreaking_spaces(repr(eval(lines[-1], context)), 30)}`</ins>  \n')
    else:
        builder.write(f'<ins>`{pad_with_nonbreaking_spaces("", 30)}`</ins>  \n')

def pad_with_nonbreaking_spaces(text, n):
    return f'{text:<{n}}'.replace(' ', '&nbsp;')

def load_explanation(topic):
    builder = StringIO()  # For efficiency, as we're building a very large string
    with open(f'../text/{topic}.md') as infile:
        while line := infile.readline():
            builder.write(line)
    result = builder.getvalue()
    builder.close()
    return result

# TODO Read this from a file
topics = [
    'string_indexing',
    'string_slicing',
    'arithmetic_operators',
    'variables',
    'string_operators',
    'quotation_marks',
    'calling_functions',
    'lists',
    'comparisons',
    'types_',
    'methods',
    'list_comprehensions',
    'f_strings',
    'sets',
    'dictionaries',
    'equality',
    'tuples',
    'defining_functions',
    'if',
    'while'
    ]
pdf = MarkdownPdf()
solutions = []
# TODO Add README.md, plus a blank page to keep exercises on fronts of pages and explanations on backs
for topic in topics:
    with open(f'../text/{topic}.md') as infile:
        title = infile.readline().rstrip()
    pdf.add_section(Section(generate_exercises(topic, title)), user_css=CSS)
    pdf.add_section(Section(load_explanation(topic)))
    solutions.append(Section(generate_exercises(topic, title, True)))
for solution in solutions:
    pdf.add_section(solution, user_css=CSS)
pdf.save(f'../output/book.pdf')
