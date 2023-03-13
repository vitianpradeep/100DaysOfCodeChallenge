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
#
def timeConversion(s):
    # Write your code here
    s1=0
    if s[-2:]=='AM':
        s1 = int(s[0:2])
        if s1==12:
            s1 = str("00")
            final1 = s.replace(s[0:2],s1)
            final1 = final1.replace(s[-2:],"")
        elif s1<12:
            s1=str(abs(s1-12))
        final1 = s.replace(s[0:2],s1)
        final1 = final1.replace(s[-2:],"")
        print(final1)
        
    elif s[-2:]=='PM':
        s2=0
        s2 = int(s[0:2])
        if s2==12:
            s2 = str("00")
            final2 = s.replace(s[0:2],s2)
            final2 = final2.replace(s[-2:],"")
        elif s2<12:
            s2 = s2 + 12
            s2=str(abs(s2))
        final2 = s.replace(s[0:2],s2)
        final2 = final2.replace(s[-2:],"")
        print(final2)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    # fptr.write(result + '\n')

    # fptr.close()
