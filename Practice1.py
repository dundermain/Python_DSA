'''
This script is developed to practice some DSA questions
Date: 01/03/2023
'''
#calculate the time complextity of the following function

def foo(array):
    sum = 0
    product = 1

    for i in array:
        sum += 1

    for i in array:
        product *= 1

    print("sum = "str(sum)+", product = "+str(product))