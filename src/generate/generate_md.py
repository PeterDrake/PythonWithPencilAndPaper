from io import StringIO
from markdown_pdf import MarkdownPdf, Section

CSS = ('<style> ' +
       ' '.join(f'table th:nth-of-type({col}) {{ width: {percent}%; }}' for col, percent in {1:10, 2:45, 3:45}.items()) +
       ' </style>')
print(CSS)

def generate_exercise_markdown(topic):
    builder = StringIO()  # For efficiency, as we're building a very large string
    # add_boilerplate(builder)
    generate_exercises(topic, builder)
    load_explanation(topic, builder)
    generate_exercises(topic, builder, True)
    result = builder.getvalue()
    builder.close()
    return result

# def add_boilerplate(builder):
#     widths = ' '.join(f'table th:nth-of-type({col}) {{ width: {percent}%; }}' for col, percent in {1:10, 2:45, 3:45}.items())
#     builder.write(f'<style> {widths} </style>\n')

def generate_exercises(topic, builder, show_answers=False):
    builder.write(f'|Number|Expression|Value|\n')
    builder.write(f'|---|---|---|\n')
    with open(f'../{topic}.py') as infile:
        line = infile.readline().rstrip()  # First example includes answer
        n = 1
        builder.write(f'|{n}|`{line}`|`{eval(line)}`|\n')
        while line := infile.readline():
            line = line.rstrip()
            if line != '':
                n += 1
                builder.write(f'|{n}|`{line}`|')
                if show_answers:
                    builder.write(f'`{eval(line)}`|\n')
                else:
                    builder.write(f'| |\n')

def load_explanation(topic, builder):
    with open(f'../../text/{topic}.md') as infile:
        while line := infile.readline():
            builder.write(line)
    builder.write('\n')

topic = 'arithmetic_operators'
pdf = MarkdownPdf()
pdf.add_section(Section(generate_exercise_markdown('arithmetic_operators')),
                user_css=CSS)
pdf.save(f'../../output/{topic}.pdf')
# with open(f'../../output/{topic}.md', 'w') as outfile:
#     outfile.write(generate_exercise_markdown('arithmetic_operators'))
