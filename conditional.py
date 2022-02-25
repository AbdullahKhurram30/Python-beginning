def conditional(a,b):
    #inputs two Boolean variables representing atomic sentences a, b
    #outputs the truth value of the conditional a->b
    return not a or b
print(conditional(True,True))
print(conditional(True,False))
print(conditional(False,True))
print(conditional(False,False))