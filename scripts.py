# Algorithmic Methods of Data Mining - Homework 1
# Problem 1: Python Challenges
# Section: Introduction

# 1. Say "Hello, World!" With Python
print("Hello, World!")


# 2. Python If-Else
if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


# 3. Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a + b)
    print(a - b)
    print(a * b)


# 4. Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a // b)
    print(a / b)


# 5. Loops
n = int(input())

for i in range(n):
    print(i ** 2)


# 6. Write a Function
def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap

year = int(input())
print(is_leap(year))


# 7. Print Function
n = int(input())

for i in range(1, n + 1):
    print(i, end="")
