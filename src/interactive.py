import os
import re


def parse_exercises(filepath):
    exercises = []
    context = {}
    with open(filepath) as f:
        lines = [line.rstrip('\n') for line in f]
    buffer = []
    n = 1
    for line in lines:
        if line == '':
            if buffer:
                exercises.append(make_exercise(n, buffer, context))
                n += 1
                buffer = []
        else:
            buffer.append(line)
    if buffer:
        exercises.append(make_exercise(n, buffer, context))
    return exercises


def make_exercise(n, lines, context):
    statements = lines[:-1]
    expression = lines[-1]
    if statements:
        exec('\n'.join(statements), context)
    answer = repr(eval(expression, context))
    return {
        "number": n,
        "statements": list(statements),
        "expression": expression,
        "answer": answer,
    }


def load_explanation(topic):
    filepath = os.path.join(os.path.dirname(__file__), '..', 'text', f'{topic}.md')
    with open(filepath) as f:
        text = f.read()
    text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    text = re.sub(r'<script.*?</script>', '', text, flags=re.DOTALL)
    return text.strip()


def prompt_exercise(ex):
    print(f"\nExercise {ex['number']}:")
    for stmt in ex['statements']:
        print(f"  {stmt}")
    print(f"  {ex['expression']}")


def phase1(exercises):
    answers = {}
    print("\n=== Initial Attempt ===\n")
    print("For each exercise, type your answer and press Enter.")
    print("Press Enter without typing to skip.\n")
    for ex in exercises:
        prompt_exercise(ex)
        ans = input("Your answer: ").strip()
        answers[ex['number']] = ans if ans else None
    return answers


def phase2(explanation):
    print("\n=== Explanation ===\n")
    print(explanation)
    print()


def phase3(exercises, answers):
    print("\n=== Review ===\n")
    print("For each exercise, press Enter to keep your previous answer,")
    print("or type a new one.\n")
    for ex in exercises:
        prompt_exercise(ex)
        prev = answers[ex['number']]
        if prev is not None:
            print(f"  Your previous answer: {prev}")
        ans = input("Your answer (Enter to keep): ").strip()
        if ans:
            answers[ex['number']] = ans
    return answers


def phase4(exercises, answers):
    print("\n=== Results ===\n")
    correct = 0
    total = len(exercises)
    for ex in exercises:
        prompt_exercise(ex)
        user_ans = answers[ex['number']]
        if user_ans == ex['answer']:
            correct += 1
            print(f"  Correct! ({ex['answer']})")
        else:
            print(f"  Correct answer: {ex['answer']}")
            if user_ans is not None:
                print(f"  Your answer:    {user_ans}")
    print(f"\nScore: {correct}/{total}")
    return correct, total


def get_title(topic):
    filepath = os.path.join(os.path.dirname(__file__), '..', 'text', f'{topic}.md')
    with open(filepath) as f:
        first_line = f.readline().strip()
    if first_line.startswith('# '):
        return first_line[2:]
    return topic.replace('_', ' ').title()


def main():
    src_dir = os.path.dirname(__file__)
    text_dir = os.path.join(src_dir, '..', 'text')
    topics_file = os.path.join(text_dir, 'topics.txt')

    with open(topics_file) as f:
        topics = [line.strip() for line in f if line.strip()]

    total_correct = 0
    total_exercises = 0

    for topic in topics:
        py_path = os.path.join(src_dir, f'{topic}.py')

        if not os.path.exists(py_path):
            print(f"\nSkipping '{topic}' (no {topic}.py found)")
            continue

        try:
            exercises = parse_exercises(py_path)
        except Exception as e:
            print(f"\nError parsing {topic}.py: {e}")
            continue

        try:
            explanation = load_explanation(topic)
        except Exception as e:
            print(f"\nError loading explanation for {topic}: {e}")
            explanation = ""

        title = get_title(topic)

        print(f"\n{'=' * 50}")
        print(f"  {title}")
        print(f"{'=' * 50}")

        answers = phase1(exercises)
        phase2(explanation)
        answers = phase3(exercises, answers)
        c, t = phase4(exercises, answers)
        total_correct += c
        total_exercises += t

    print(f"\n{'=' * 50}")
    print(f"  OVERALL: {total_correct}/{total_exercises}")
    print(f"{'=' * 50}")


if __name__ == '__main__':
    main()
