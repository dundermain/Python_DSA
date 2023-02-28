'''
FInd the results of exponents
'''

def power(x, n):
    assert x>=0 and n>=0, 'The number and exponent should be positive integers'

    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
    

print(power(2,3))
