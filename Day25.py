#!/bin/python3

import math
import os
import random
import re
import sys

def superReducedString(s):
    while True:
        # Flag to check if any adjacent duplicates were found
        found_duplicates = False
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                s = s[:i]+s[i+2:]
                found_duplicates = True
                break
        if not found_duplicates:
            # No more adjacent duplicates found, return the final string
            return s if s else "Empty String"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
