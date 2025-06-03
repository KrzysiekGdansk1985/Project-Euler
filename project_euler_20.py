"""
Factorial Digit Sum
Problem 20
n! means n x (n-1) x ... x 3 x 2 x 1.

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10!
is 3+6+2+8+8+0+0=27.

Find the sum of the digits in the number 100!.
"""

k=1

for i in range(1, 101):
    k *= i

x = str(k)
sum_num = 0

for i in range(len(x)):
    sum_num += int(x[i])

print("This number is:", sum_num)
