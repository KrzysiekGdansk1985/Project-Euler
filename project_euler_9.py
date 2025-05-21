"""
Special Pythagorean Triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c
for which, a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which
a + b + c = 1000.
Find the product abc.
"""



x = []
i = 1
find = False
while i <= 998:
    j = 1
    while j <= 998:
        k = 1
        while k <= 998:
            if i < j < k and pow(i, 2) + pow(j, 2) == pow(k, 2) and i + j + k == 1000:
                find = True
                break
            k += 1
        if find == True:
            break
        j += 1
    if find == True:
        break
    i += 1
            


print("These numbers are:", i, j, k)
print("Product is", i*j*k)




    
