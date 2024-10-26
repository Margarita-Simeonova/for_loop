def vowels_sum(string):
    total_sum = 0
    for el in string:
        if el == "a":
            total_sum += 1
        elif el == "e":
            total_sum += 2
        elif el == "i":
            total_sum += 3
        elif el == "o":
            total_sum += 4
        elif el == "u":
            total_sum += 5

    return total_sum


text = input()
print(vowels_sum(text))
