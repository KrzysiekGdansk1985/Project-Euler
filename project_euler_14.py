"""
Longest Collatz Sequence
Problem 14
The following iterative sequence is defined
for the set of positive integers:

n -> n/2 (n is even)
n -> 3n+1 (n is odd)

Using the rule above and starting with 13,
we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet
(Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

max_lenght = 1
k = 1
t =[0]
for i in range(1,10**6):
    k = i
    chain = 1
    while k > 1:
        chain += 1
        if k % 2 == 0:
            k = k/2
        else:
            k = 3*k + 1
    if chain > max_lenght:
        max_lenght = chain
    t.append(chain)
        
print("This number is:", t.index(max_lenght))




