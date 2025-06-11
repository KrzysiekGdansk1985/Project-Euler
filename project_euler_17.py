"""
Number Letter Counts
Problem 17
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are
3+3+5+4+4=19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive
were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example,
342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers
is in compliance with British usage.
"""

sum_of_letters = 0

for i in range(1, 100):
    x = str(i)
    
    if len(x) == 1:
        if x[0] in ['1', '2', '6']:
            sum_of_letters += 3
        elif x[0] in ['4', '5', '9']:
            sum_of_letters += 4
        else:
            sum_of_letters += 5        

    elif len(x) == 2:
        if x[0] == '1':
            if x[1] in ['0']:
                sum_of_letters += 3
            elif x[1] in ['1', '2']:
                sum_of_letters += 6
            elif x[1] in ['3', '4', '8', '9']:
                sum_of_letters += 8
            elif x[1] in ['5', '6']:
                sum_of_letters += 7
            else:
                sum_of_letters += 9
        elif x[0] in ['2', '3', '8', '9']:
            if x[1] in ['0']:
                sum_of_letters += 6                
            elif x[1] in ['1', '2', '6']:
                sum_of_letters += 9
            elif x[1] in ['4', '5', '9']:
                sum_of_letters += 10
            else:
                sum_of_letters += 11
        elif x[0] in ['4', '5', '6']:
            if x[1] in ['0']:
                sum_of_letters += 5                
            elif x[1] in ['1', '2', '6']:
                sum_of_letters += 8
            elif x[1] in ['4', '5', '9']:
                sum_of_letters += 9
            else:
                sum_of_letters += 10
        else:
            if x[1] in ['0']:
                sum_of_letters += 7                
            elif x[1] in ['1', '2', '6']:
                sum_of_letters += 10
            elif x[1] in ['4', '5', '9']:
                sum_of_letters += 11
            else:
                sum_of_letters += 12            

x = sum_of_letters

x = 10*x
    
x += (9*99*10 + 9*7 + 300*3 + 300*4 + 300*5 + 11)
        

print("This number is:", x)





    
