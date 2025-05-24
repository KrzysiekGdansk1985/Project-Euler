"""
Summation of Primes
Problem 10
The sum of the primes below 10
is 2+3+5+7=17.
Find the sum of all the primes below two million.
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

suma = 0
i = 2

while i < 2000000:
    if is_prime(i):
        suma += i
    i += 1

print("This number is:", suma)




    
