"""
Sum Square Difference 
Problem 6
The sum of the squares of the first ten natural numbers is 385.
The square of the sum of the first ten natural numbers is 3025.
Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025-385=2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

i = 1
sum_1 = 0
while i <= 100:
    sum_1 += i
    i += 1
x = pow(sum_1, 2)

i = 1
y = 0
while i <= 100:
    y += pow(i, 2)
    i += 1

print("Find the number is:", x - y)



    
