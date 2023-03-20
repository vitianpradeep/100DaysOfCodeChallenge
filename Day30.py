#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# def getTotalX(a, b):
    # Write your code here
def getTotalX(list1, list2):
    # Create an empty list to store the result
    result = []
    
    # Check each integer between the maximum value in list1 and the minimum value in list2
    for i in range(max(list1), min(list2)+1):
        
        # Check if i is a factor of all elements in list2
        if all([j % i == 0 for j in list2]):
            
            # Check if all elements in list1 are factors of i
            if all([i % j == 0 for j in list1]):
                
                # Add i to the result list
                result.append(i)
    
    # Return the result list length
    return len(result)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
