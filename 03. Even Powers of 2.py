def even_powers_of_2(numb):

    for n in range(numb + 1):
        if n % 2 == 0:
            print(2 ** n)


number = int(input())
even_powers_of_2(number)
