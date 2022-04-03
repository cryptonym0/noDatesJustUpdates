# https://www.hackerrank.com/challenges/counting-valleys/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    # only care for valleys
    # start at 0
    # U is posative
    # D is negative
    # boolean for is below
    below_sea = False
    val = 0
    x = 0
    for c in s:
        if c is "U":
            x = x + 1
        else:
            x = x - 1
        # determine location
        if x < 0:
            below_sea = True
        if below_sea and x == 0:
            val = val + 1
            below_sea = False
    return val


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + "\n")

    fptr.close()
