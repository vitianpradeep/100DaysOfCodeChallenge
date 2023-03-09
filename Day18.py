#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    d1=0
    d2=0
    for i in range (0,n):
        d1 = arr[i][i]+d1
        d2 = arr[i][n-1-i]+d2
        diff = abs(d1-d2)
    # diff = d = abs((arr[0][0]+arr[1][1]+arr[2][2])-(arr[0][2]+arr[1][1]+arr[2][0]))
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
