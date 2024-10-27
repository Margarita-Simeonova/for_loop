def histogram(numbs_count):
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0

    for _ in range(numbs_count):
        number = int(input())
        if number < 200:
            p1 += 1
        elif 200 <= number < 400:
            p2 += 1
        elif 400 <= number < 600:
            p3 += 1
        elif 600 <= number < 800:
            p4 += 1
        elif 800 <= number:
            p5 += 1

    per_p1 = p1 / numbs_count * 100
    per_p2 = p2 / numbs_count * 100
    per_p3 = p3 / numbs_count * 100
    per_p4 = p4 / numbs_count * 100
    per_p5 = p5 / numbs_count * 100

    return f"{per_p1:.2f}%\n{per_p2:.2f}%\n{per_p3:.2f}%\n{per_p4:.2f}%\n{per_p5:.2f}%"


numbers_count = int(input())
print(histogram(numbers_count))
