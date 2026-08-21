from io import StringIO
from markdown_pdf import MarkdownPdf, Section

CSS = 'body {line-height: 2}\n'

def generate_exercises(topic, title, show_answers=False):
    context = {}
    builder = StringIO()  # For efficiency, as we're building a very large string
    if show_answers:
        builder.write(title + ' (Solutions)\n')
    else:
        builder.write(title + ' (Exercises)\n')
    new_question = True
    first_answer_still_needed = True
    with open(f'{topic}.py') as infile:
        previous_line = infile.readline().rstrip()  # First example includes answer
        n = 1
        while line := infile.readline():
            line = line.rstrip()
            if line == '':
                generate_question(n, previous_line, builder, context, True, first_answer_still_needed or show_answers, new_question)
                new_question = True
                first_answer_still_needed = False
                n += 1
            elif previous_line != '':
                generate_question(n, previous_line, builder, context, False, first_answer_still_needed or show_answers, new_question)
                new_question = False
            previous_line = line
        if previous_line != '':
            generate_question(n, previous_line, builder, context, True, first_answer_still_needed or show_answers, new_question)
    result = builder.getvalue()
    builder.close()
    return result

def generate_question(n, line, builder, context, last_line, show_answer=False, new_question=True):
    padded_line = pad_with_nonbreaking_spaces(line, 30, True) + '&nbsp;&nbsp;'
    # print(f'LINE is <{line}>, last_line is {last_line}')
    if last_line:
        # eval(line, context)
        if new_question:
            builder.write(f'{n}. `{padded_line}`')
        else:
            # TODO Adjust for length of str(n)
            builder.write(f'   `{padded_line}`')
        if show_answer:
            builder.write(f'<ins>`{pad_with_nonbreaking_spaces(repr(eval(line, context)), 30, False)}`</ins>  \n')
        else:
            builder.write(f'<ins>`{pad_with_nonbreaking_spaces("", 30, False)}`</ins>  \n')
    else:
        exec(line, context)
        if new_question:
            builder.write(f'{n}. `{padded_line}`  \n')
        else:
            # TODO Adjust for length of str(n)
            builder.write(f'   `{padded_line}`  \n')

def pad_with_nonbreaking_spaces(text, n, left):
    result = ''
    if left:
        result += '&nbsp;' * (n - len(text))
    result += text.replace(' ', '&nbsp;')  # Otherwise markdown collapses multiple spaces
    if not left:
        result += '&nbsp;' * (n - len(text))
    return result

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
    'tuples'
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
