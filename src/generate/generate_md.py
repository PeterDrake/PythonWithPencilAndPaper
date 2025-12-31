def generate_exercise_markdown(topic):
    with open(f'../../output/{topic}.md', 'w') as outfile:
        widths = ' '.join(f'table th:nth-of-type({col}) {{ width: {percent}%; }}' for col, percent in {1:10, 2:45, 3:45}.items())
        outfile.write(f'<style> {widths} </style>\n')
        outfile.write(f'|Number|Expression|Value|\n')
        outfile.write(f'|---|---|---|\n')
        with open(f'../{topic}.py') as infile:
            line = infile.readline().rstrip()  # First example includes answer
            n = 1
            outfile.write(f'|{n}|`{line}`|`{eval(line)}`|\n')
            while line := infile.readline():
                line = line.rstrip()
                if line != '':
                    n += 1
                    outfile.write(f'|{n}|`{line}`| |\n')


generate_exercise_markdown('arithmetic_operators')

