import sys


def half_sum_element(numb):

    max_num = -sys.maxsize
    sum_numbs = 0

    for num in range(numb):
        number = int(input())
        if number > max_num:
            max_num = number

        sum_numbs += number

    if max_num == sum_numbs / 2:
        return f"Yes\nSum = {max_num}"
    else:
        sum_others = sum_numbs - max_num
        return f"No\nDiff = {abs(max_num - sum_others)}"


numbers_count = int(input())
print(half_sum_element(numbers_count))
