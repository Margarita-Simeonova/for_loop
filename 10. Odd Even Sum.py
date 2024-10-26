def odd_and_even_sum(numbs_count):
    odd_sum = 0
    even_sum = 0
    for i in range(numbs_count):
        numb = int(input())
        if i % 2 == 0:
            even_sum += numb
        else:
            odd_sum += numb

    if even_sum == odd_sum:
        return f"Yes\nSum = {even_sum}"
    else:
        return f"No\nDiff = {abs(even_sum - odd_sum)}"


numbers_count = int(input())
print(odd_and_even_sum(numbers_count))
