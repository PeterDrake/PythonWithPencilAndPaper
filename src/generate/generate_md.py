def generate_exercise_markdown(topic):
    with open(f'../../output/{topic}.md', 'w') as outfile:
        outfile.write('<style> table th:first-of-type { width: 50%; } table th:nth-of-type(2) { width: 50%; } </style>\n')
        outfile.write(f'|{'Expression'}|{'Value'}|\n')
        outfile.write(f'|---|---|\n')
        with open(f'../{topic}.py') as infile:
            line = infile.readline().rstrip()  # First example includes answer
            outfile.write(f'|`{line}`|`{eval(line)}`|\n')
            while line := infile.readline():
                line = line.rstrip()
                if line != '':
                    outfile.write(f'|`{line}`| |\n')


generate_exercise_markdown('arithmetic_operators')

