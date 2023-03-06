'''
This script is developed to practice some DSA questions
Date: 06/03/2023
'''

#which of the follwing is NOT equivalent ot O(N)
    #O(N+P) where P<N/2
    #O(2N)
    #O(N + logN)
    #O(N + NlogN) (ANSWER)
    #O(N+M) (Dont neglect M from here as it can be anything)

#Find the runtime of the below code
def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
#

