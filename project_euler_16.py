"""
Power Digit Sum
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""

x_int = 2**1000
x_str = str(x_int)
len_x = len(x_str)

suma = 0

for i in range(len_x):
    suma += int(x_str[i])

print("This number is:", suma)
