def left_and_right_sum(numbs_count):

    first_group = 0
    second_group = 0

    for i in range(2):
        for _ in range(numbs_count):
            number = int(input())
            if i == 0:
                first_group += number
            else:
                second_group += number

    if first_group == second_group:
        return f"Yes, sum = {first_group}"
    else:
        return f"No, diff = {abs(first_group - second_group)}"


numbers_count = int(input())
print(left_and_right_sum(numbers_count))
