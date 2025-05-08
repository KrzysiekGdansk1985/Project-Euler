"""
Largest Prime Factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
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

largest_prime_factor = 1

j = 2
z = math.floor(math.sqrt(600851475143))
while j <= z:
    if 600851475143 % j == 0:
        if is_prime(j) and j > largest_prime_factor:
            largest_prime_factor = j
        a = int(600851475143/j)
        if is_prime(a) and a > largest_prime_factor:
            largest_prime_factor = a
    j += 1

if largest_prime_factor == 1:
    largest_prime_factor = 600851475143
    
print("The largest prime factor of the number 600851475143 is", largest_prime_factor)
    
