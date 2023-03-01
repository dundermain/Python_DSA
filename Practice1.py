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
#the answer is O(n)

#calculate the time complexity of below code
def printPairs(array):
    for i in array:
        for j in array:
            print(str(i)+","+str(j))
#THe answer is o(n^2)

#calculate the time complexity of the following code
def printUnorderedPAirs(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            print(array[i] + "," + array[j])
#THe answer is O(n^2)

