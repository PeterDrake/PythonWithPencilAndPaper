from io import StringIO
from markdown_pdf import MarkdownPdf, Section

CSS = 'body {line-height: 2}\n'

def generate_exercises(topic, title, show_answers=False):
    builder = StringIO()  # For efficiency, as we're building a very large string
    if show_answers:
        builder.write(title + ' (Solutions)\n')
    else:
        builder.write(title + ' (Exercises)\n')
    with open(f'../{topic}.py') as infile:
        line = infile.readline().rstrip()  # First example includes answer
        n = 1
        generate_question(n, line, builder, True)
        while line := infile.readline():
            line = line.rstrip()
            if line != '':
                n += 1
                generate_question(n, line, builder, show_answers)
    result = builder.getvalue()
    builder.close()
    return result

def generate_question(n, line, builder, show_answer=False):
    padded_line = pad_with_nonbreaking_spaces(line, 30, True) + '&nbsp;&nbsp;'
    builder.write(f'{n}. `{padded_line}`')
    if show_answer:
        builder.write(f'<ins>`{pad_with_nonbreaking_spaces(str(eval(line)), 30, False)}`</ins>  \n')
    else:
        builder.write(f'<ins>`{pad_with_nonbreaking_spaces("", 30, False)}`</ins>  \n')

def pad_with_nonbreaking_spaces(text, n, left):
    result = ''
    if left:
        result += '&nbsp;' * (n - len(text))
    result += text
    if not left:
        result += '&nbsp;' * (n - len(text))
    return result

def load_explanation(topic):
    builder = StringIO()  # For efficiency, as we're building a very large string
    with open(f'../../text/{topic}.md') as infile:
        while line := infile.readline():
            builder.write(line)
    result = builder.getvalue()
    builder.close()
    return result

# TODO Read this from a file
topics = ['string_indexing',
          'string_slicing',
          'arithmetic_operators',
          'variables']
pdf = MarkdownPdf()
solutions = []
for topic in topics:
    with open(f'../../text/{topic}.md') as infile:
        title = infile.readline().rstrip()
    pdf.add_section(Section(generate_exercises(topic, title)), user_css=CSS)
    pdf.add_section(Section(load_explanation(topic)))
    solutions.append(Section(generate_exercises(topic, title, True)))
for solution in solutions:
    pdf.add_section(solution, user_css=CSS)
pdf.save(f'../../output/book.pdf')
