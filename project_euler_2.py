"""
Even Fibonacci Numbers
Problem 2
Each new term in the Fibonacci sequence is generated
by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even valued terms.
"""
sum = 2
a = 1
b = 2
pom = a + b

while pom <= 4*10**6:
    a = b
    b = pom
    pom = a + b
    if pom % 2 == 0 and pom <= 4*10**6:
        sum += pom

print("Sum =", sum)
