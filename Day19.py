#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    # for i in range (n):
    i=0
    count2=0
    count1=0
    count3=0
    s1=0
    s2=0
    s3=0
    for i in range (n):
        if arr[i]>0:
            count1+=1
            s1 = count1/n
        if arr[i]<0:
            count2+=1
            s2 = count2/n
        if arr[i]==0:
            count3+=1
            s3 = count3/n
    print(s1)
    print(s2)
    print(s3)        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
