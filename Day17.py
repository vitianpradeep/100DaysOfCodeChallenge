#!/bin/python3

import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    # Write your code here
    sum =0
    for i in range (0, ar_count):
        sum = sum + ar[i]
    return sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
