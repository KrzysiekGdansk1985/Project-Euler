"""
Largest Palindrome Product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
i = 100
k = 0
pal_num = 0
while i <= 999:
    j = 100
    while j <= 999:
        k = i * j
        if str(k) == str(k)[::-1]:
            if k > pal_num:
                pal_num = k
        j += 1
    i += 1 	

if pal_num > 0:
   print("This number is", pal_num)   
