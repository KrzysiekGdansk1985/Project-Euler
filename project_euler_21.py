"""
Amicable Numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a)=b and d(b)=a where a=/=b then a and b
are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55
and 110; therefore d(220)=284. The proper divisors of 284 are 1,2,4,71
and 142; so d(284)=220.

Evaluate the sum of all the amicable numbers under 10000.
"""

y = []

for i in range(2, 10000):
    j = 1
    k = 0
    while j < i:
        if i % j == 0:
            k += j
        j += 1
        
    z = 1
    x = 0
    while z < k:
        if k % z == 0:
            x += z
        z += 1
    if i == x and i != k:
        y.append(i)
        y.append(k)

print(sum(y)/2)
print(y)
    
    
            
    
    
