#!/bin/python

'''
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography
During his last hike he took exactly n steps.
For every step he took, he noted if it was an uphill, U , or a downhill, D  step. 
Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude. We define the following terms:
1)A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
2)A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

Sample Input:
8
uddduduu

Sample output:
1
'''
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    v = 0
    s = list(s)
    for c in s:
        if(c=='U'):
            ++level
        if(c=='D'):
            --level
        if level == 0 and c == 'U':
                ++v
    return v
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
