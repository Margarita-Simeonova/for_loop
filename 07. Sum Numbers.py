def sum_numbers(numbers_count):
    total_sum = 0
    for _ in range(numbers_count):
        numb = int(input())
        total_sum += numb

    return total_sum


count_of_numbers = int(input())
print(sum_numbers(count_of_numbers))
