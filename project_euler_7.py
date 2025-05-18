"""
10 001st Prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10001st prime number?
"""

import math

def is_prime(x):
    y = math.floor(math.sqrt(x))
    i = 2
    while i <= y:
        if x % i == 0:
            return False
        i += 1
    return True

j = 0
k = 2
while True:
    if is_prime(k):
        j += 1
    if  j == 10001:
        break
    k += 1

print("This number is:", k) 




    
