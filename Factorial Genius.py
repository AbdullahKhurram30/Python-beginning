import math

def factorial(n):
    if n > 0:
        multiply_numbers = range(1, n+1)
        p = 1
        for number in multiply_numbers:
            p *= number
        if p == math.factorial(n):
            return p 
    else:
        return "Kindly insert a non-negative number."
