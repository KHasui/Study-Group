"""
Exercise 1: the function 'factorial(n)' calculates n!
"""

def factorial(n):
    
    fval = 1; # initial value of n
    
    for i in range(n):    # i in [0,...,n]
        fval = fval*(n-i) # iteration of n*(n-1)*...*1
    return fval
