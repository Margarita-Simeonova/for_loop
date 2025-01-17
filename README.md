# for_loop
## Start with loops

# For loop - lab

### Tasks:

01. Numbers from 1 to 100:

Write a program that prints the numbers 1 to 100, each on a new line.

########

02. Numbers 1...N with Step 3:

Write a program that prints the numbers 1 to 100, each on a new line.

########

03. Even Powers of 2

Write a program that reads a number n entered by the user and prints the even powers of 2 ≤ 2^n: 2^6, 2^2, 2^4, 2^6, …, 2^n.

########

04. Numbers N...1

Write a program that reads a positive integer n entered by the user and prints the numbers from n to 1 in reverse order. The entered number n will always be greater than 1.

########

05. Character Sequence

Write a program that reads text (string) entered by the user and prints each character of the text on a separate line.

########

06. Vowels Sum:


To write a program that reads text (string) entered by the user and calculates and prints the sum of the vowel values ​​according to the table below:

letter a e i o u

value  1 2 3 4 5

########

07. Sum Numbers:

To write a program that reads n-th number of integers entered by the user and sums them.

· The number of numbers n is entered from the first line of the input.

· One whole number is entered from the next n lines.

The program must read the numbers, add them, and print the sum.

########

08. Number sequence:

Write a program that reads n number of integers. Print the largest and smallest number among those entered.

########

09. Left and Right Sum:

Write a program that reads 2*n number of user-supplied integers and checks whether the sum of the first n numbers (left sum) is equal to the sum of the second n numbers (right sum). 

If there is a tie, print " Yes, sum = " + the sum;

otherwise it prints " No, diff = " + the difference. The difference is calculated as a positive number (in absolute value).

########

10. Odd Even Sum:

Write a program that reads n-th number of integers supplied by the user and checks whether the sum of the numbers in even positions is equal to the sum of the numbers in odd positions. If there is a tie, print two lines:

"Yes" and on a new line "Sum = " + the sum; 

otherwise print "No" and on a new line "Diff = " + the difference. The difference is calculated in absolute value.


## For Loop - Exercise

01. Numbers Ending in 7:

Write a program that prints the numbers in the range [1…1000] that end in 7.

########

02. Half Sum Elemen:

Write a program that reads n-th number of integers entered by the user and checks if there is a number among them that is equal to the sum of all the others. 

If there is such an element, print "Yes" and on a new line "Sum = " + its value
    
If there is no such element, print "No" and on a new line "Diff = " + the difference between the largest element and the sum of the others (by absolute value)

########

03. Histogram:

Given n integers in the interval [1…1000]. Of these, some percentage p1 are below 200, another percentage p2 are from 200 to 399, another percentage p3 are from 400 to 599, another percentage p4 are from 600 to 799 and the remaining p5 percentage are from 800 and up. To write a program that calculates and prints the percentages p1, p2, p3, p4 and p5.

Input:
The first line of the input contains the integer n (1 ≤ n ≤ 1000) – number of numbers. On the next n lines there is one whole number in the interval [1...1000] - the numbers on which the histogram should be calculated.


Output:
Print the histogram to the console - 5 lines, each containing a number between 0% and 100%, to two decimal places, eg 25.00%, 66.67%, 57.14%.

########

04. Clever Lily:

Lily is now N years old. For every birthday she gets a present. 

• For odd birthdays (1, 3, 5...n) she gets toys.

• For even birthdays (2, 4, 6...n) she receives money. 

For the second birthday, he receives BGN 10.00, and the amount increases by BGN 10.00 for each subsequent even birthday (2 -> 10, 4 -> 20, 6 -> 30...etc.). Over the years, Lily has secretly saved the money. Lily's brother, in the years that she receives money, takes BGN 1.00 from them. Lily sold the toys received in the years, each for P leva and added the amount to the money saved. With the money, she wanted to buy a washing machine for BGN X. Write a program to calculate how much money she has collected and whether she has enough to buy a washing machine.

Input:

The program reads 3 numbers entered by the user on separate lines:

• Lily's age - an integer

• The price of the washing machine - float

• Unit price of a toy - an integer

Output:

To print one line to the console:

• If Lily's money is enough:

◦ "Yes! {N}" - where N is the remaining money after the purchase

• If the money is not enough:

◦ "No! {M}" - where M is the amount missing

The numbers N and M must be formatted to the second decimal place.
