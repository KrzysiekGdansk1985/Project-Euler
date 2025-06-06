"""
Lattice Paths
Problem 15
Starting in the top left corner of a 2x2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""

x = 1

for i in range(21, 41):
    x *= i
for i in range(1, 21):
    x /= i
print("This number is:", x)
