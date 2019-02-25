#!/bin/python
'''
Emma is playing a new mobile game involving n clouds numbered from 0 to n-1. A player initially starts out on cloud c0, and they must jump to cloud cn-1. In each step, she can jump from any cloud i to cloud i+1 or cloud i+2.


'''
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    c = list(c)
    res = 0
    i = 0
    while i < n-1:
        if i+2<n and c[i+2] == 0:
            i = i+2
            res += 1
        else:
            i = i+1
            res += 1
    return(res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
