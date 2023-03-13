#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the s'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def timeConversion(s):
    s1 = 0
    if s[-2:] == 'AM':
        s1 = int(s[0:2])
        if s1 == 12:
            s1 = 0
        final1 = "{:02d}".format(s1) + s[2:-2]
        print(final1)
    elif s[-2:] == 'PM':
        s2 = int(s[0:2])
        if s2 != 12:
            s2 = s2 + 12
        final2 = "{:02d}".format(s2) + s[2:-2]
        print(final2)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    # fptr.write(result + '\n')

    # fptr.close()
