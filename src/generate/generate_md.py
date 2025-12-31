from io import StringIO
from markdown_pdf import MarkdownPdf, Section

CSS = 'table { width:100%; table-layout:fixed; }\n'
# CSS = ''
CSS += 'tr th:nth-of-type(1) { width: 10%; }\n'
CSS += 'tr th:nth-of-type(2) { width:45%; }\n'
CSS += 'tr th:nth-of-type(3) { width:45%; }\n'
# CSS += '</style>'+
       # ' '.join(f'table th:nth-of-type({col}) {{ table-layout: fixed width: {percent}%; }}' for col, percent in {1:10, 2:45, 3:45}.items()) +
       # ' </style>')
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

def generate_exercises(topic, show_answers=False):
    builder = StringIO()  # For efficiency, as we're building a very large string
    # builder.write(f'|Number|Expression|Value|\n')
    # builder.write(f'|:---|:---|:---|\n')
    with open(f'../{topic}.py') as infile:
        line = infile.readline().rstrip()  # First example includes answer
        n = 1
        builder.write(f'{n}. `{line:<30}`  \n`{eval(line)}`  \n')
        builder.write('  \n')
        while line := infile.readline():
            line = line.rstrip()
            if line != '':
                n += 1
                builder.write(f'{n}. `{line:<30}`  \n')
                if show_answers:
                    builder.write(f'<ins>`{eval(line)}`</ins>  \n')
                else:
                    builder.write(f'<ins>{'&nbsp;'*20}</ins>  \n')
                builder.write('  \n')
    result = builder.getvalue()
    builder.close()
    return result

def load_explanation(topic):
    builder = StringIO()  # For efficiency, as we're building a very large string
    with open(f'../../text/{topic}.md') as infile:
        while line := infile.readline():
            builder.write(line)
    result = builder.getvalue()
    builder.close()
    return result

topic = 'arithmetic_operators'
pdf = MarkdownPdf()
pdf.add_section(Section(generate_exercises('arithmetic_operators')))
pdf.add_section(Section(load_explanation('arithmetic_operators')))
pdf.add_section(Section(generate_exercises('arithmetic_operators', True)))
pdf.save(f'../../output/{topic}.pdf')
# with open(f'../../output/{topic}.md', 'w') as outfile:
#     outfile.write(generate_exercise_markdown('arithmetic_operators'))
