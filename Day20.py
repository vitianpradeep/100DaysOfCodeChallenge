


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range (n,0,-1):
        for j in range (1,n+1,1):
            if j<i:
                print(" ",end="")
            elif j>=i:
                print("#",end="")
        print("")
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
