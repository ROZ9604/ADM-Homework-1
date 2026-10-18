
# Algorithmic Methods of Data Mining - Homework 1
# Problem 1: Python Challenges


# ============================================================
# SECTION 1: INTRODUCTION
# ============================================================

# 1. Say "Hello, World!" With Python
def hello_world():
    print("Hello, World!")


# 2. Python If-Else
def python_if_else():
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


# 3. Arithmetic Operators
def arithmetic_operators():
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)


# 4. Python: Division
def python_division():
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)


# 5. Loops
def loops():
    n = int(input())
    for i in range(n):
        print(i ** 2)


# 6. Write a Function
def write_a_function():
    def is_leap(year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        return False

    year = int(input())
    print(is_leap(year))


# 7. Print Function
def print_function():
    n = int(input())
    for i in range(1, n + 1):
        print(i, end="")
    print()


# ============================================================
# SECTION 2: BASIC DATA TYPES
# ============================================================

# 1. List Comprehensions
def list_comprehensions():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]
    print(result)


# 2. Find the Runner-Up Score
def runner_up_score():
    n = int(input())
    scores = list(map(int, input().split()))
    unique_scores = sorted(set(scores))
    print(unique_scores[-2])


# 3. Nested Lists
def nested_lists():
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    grades = sorted(set(student[1] for student in students))
    second_lowest = grades[1]

    names = sorted(
        student[0] for student in students
        if student[1] == second_lowest
    )

    for name in names:
        print(name)


# 4. Finding the Percentage
def finding_the_percentage():
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        student_marks[name] = list(map(float, line))

    query_name = input()
    marks = student_marks[query_name]
    print(f"{sum(marks) / len(marks):.2f}")


# 5. Lists
def lists():
    n = int(input())
    numbers = []

    for _ in range(n):
        command = input().split()
        action = command[0]

        if action == "insert":
            numbers.insert(int(command[1]), int(command[2]))
        elif action == "print":
            print(numbers)
        elif action == "remove":
            numbers.remove(int(command[1]))
        elif action == "append":
            numbers.append(int(command[1]))
        elif action == "sort":
            numbers.sort()
        elif action == "pop":
            numbers.pop()
        elif action == "reverse":
            numbers.reverse()


# 6. Tuples
def tuples():
    n = int(input())
    values = tuple(map(int, input().split()))

    # The HackerRank Editorial was consulted for this challenge.
    print(hash(values))


# ============================================================
# SECTION 3: SETS
# ============================================================

# Introduction to Sets
def introduction_to_sets():
    n = int(input())
    numbers = set(map(float, input().split()))
    print(sum(numbers) / len(numbers))


# ============================================================
# SECTION 4: MATHEMATICS
# ============================================================

# Find Angle MBC
def find_angle_mbc():
    import math

    ab = int(input())
    bc = int(input())

    angle = math.degrees(math.atan2(ab, bc))
    print(f"{int(angle + 0.5)}\N{DEGREE SIGN}")


# ============================================================
# SECTION 5: NUMPY
# ============================================================

# Arrays: NumPy
def numpy_arrays():
    import numpy as np

    np.set_printoptions(legacy="1.13")
    n, m = map(int, input().split())
    print(np.eye(n, m))


# Arrays: Mathematics
def arrays_mathematics():
    import numpy as np

    n, m = map(int, input().split())
    a = np.array([
        list(map(int, input().split()))
        for _ in range(n)
    ])
    b = np.array([
        list(map(int, input().split()))
        for _ in range(n)
    ])

    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(a ** b)


# ============================================================
# SECTION 6: STRINGS
# ============================================================

# 1. sWAP cASE
def swap_case():
    print(input().swapcase())


# 2. String Split and Join
def string_split_and_join():
    line = input()
    print("-".join(line.split()))


# 3. What's Your Name?
def whats_your_name():
    first_name = input()
    last_name = input()
    print(
        f"Hello {first_name} {last_name}! "
        "You just delved into python."
    )


# 4. Mutations
def mutate_string():
    string = input()
    position, character = input().split()

    letters = list(string)
    letters[int(position)] = character
    print("".join(letters))


# 5. Find a String
def find_a_string():
    string = input().strip()
    sub_string = input().strip()
    count = 0

    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1

    print(count)


# 6. String Validators
def string_validators():
    s = input()

    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))


# 7. Text Alignment
def text_alignment():
    thickness = int(input())
    c = "H"

    # Top cone
    for i in range(thickness):
        print(
            (c * i).rjust(thickness - 1)
            + c
            + (c * i).ljust(thickness - 1)
        )

    # Top pillars
    for _ in range(thickness + 1):
        print(
            (c * thickness).center(thickness * 2)
            + (c * thickness).center(thickness * 6)
        )

    # Middle belt
    for _ in range((thickness + 1) // 2):
        print((c * thickness * 5).center(thickness * 6))

    # Bottom pillars
    for _ in range(thickness + 1):
        print(
            (c * thickness).center(thickness * 2)
            + (c * thickness).center(thickness * 6)
        )

    # Bottom cone
    for i in range(thickness):
        print(
            (
                (c * (thickness - i - 1)).rjust(thickness)
                + c
                + (c * (thickness - i - 1)).ljust(thickness)
            ).rjust(thickness * 6)
        )


# 8. Text Wrap
def text_wrap():
    import textwrap

    string = input()
    max_width = int(input())
    print(textwrap.fill(string, max_width))


# 9. Designer Door Mat
def designer_door_mat():
    n, m = map(int, input().split())

    for i in range(n // 2):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(m, "-"))

    print("WELCOME".center(m, "-"))

    for i in range(n // 2 - 1, -1, -1):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(m, "-"))


# 10. String Formatting
def string_formatting():
    number = int(input())
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        print(
            str(i).rjust(width),
            oct(i)[2:].rjust(width),
            hex(i)[2:].upper().rjust(width),
            bin(i)[2:].rjust(width)
        )


# 11. Capitalize!
def capitalize():
    s = input()
    print(" ".join(word.capitalize() for word in s.split(" ")))


# 12. The Minion Game
def minion_game():
    string = input()
    kevin = 0
    stuart = 0
    n = len(string)

    for i in range(n):
        if string[i] in "AEIOU":
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


# 13. Merge the Tools!
def merge_the_tools():
    string = input()
    k = int(input())

    for i in range(0, len(string), k):
        substring = string[i:i + k]
        result = ""

        for char in substring:
            if char not in result:
                result += char

        print(result)


# ============================================================
# CHALLENGE RUNNER
# Run only the challenge you select.
# Example: python scripts.py swap_case
# ============================================================

CHALLENGES = {
    # Introduction
    "hello": hello_world,
    "if_else": python_if_else,
    "arithmetic_operators": arithmetic_operators,
    "division": python_division,
    "loops": loops,
    "leap_year": write_a_function,
    "print_function": print_function,

    # Basic Data Types
    "list_comprehensions": list_comprehensions,
    "runner_up": runner_up_score,
    "nested_lists": nested_lists,
    "percentage": finding_the_percentage,
    "lists": lists,
    "tuples": tuples,

    # Sets
    "introduction_to_sets": introduction_to_sets,

    # Mathematics
    "angle_mbc": find_angle_mbc,

    # NumPy
    "numpy_arrays": numpy_arrays,
    "arrays_mathematics": arrays_mathematics,

    # Strings
    "swap_case": swap_case,
    "split_join": string_split_and_join,
    "whats_your_name": whats_your_name,
    "mutate_string": mutate_string,
    "find_string": find_a_string,
    "string_validators": string_validators,
    "text_alignment": text_alignment,
    "text_wrap": text_wrap,
    "door_mat": designer_door_mat,
    "string_formatting": string_formatting,
    "capitalize": capitalize,
    "minion_game": minion_game,
    "merge_the_tools": merge_the_tools,
}


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Choose one challenge key:")
        for key in CHALLENGES:
            print(" ", key)
        print("\nExample: python scripts.py swap_case")
        sys.exit(0)

    challenge_key = sys.argv[1].lower()

    if challenge_key not in CHALLENGES:
        print("Unknown challenge:", challenge_key)
        print("Run `python scripts.py` to see the available keys.")
        sys.exit(1)

    CHALLENGES[challenge_key]()
