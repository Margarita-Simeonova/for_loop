import sys


def number_sequence(numbers_count):
    max_num = -sys.maxsize
    min_num = sys.maxsize

    for _ in range(numbers_count):
        number = int(input())
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number

    return f"Max number: {max_num}\nMin number: {min_num}"


count = int(input())
print(number_sequence(count))
