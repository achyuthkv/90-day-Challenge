'''
John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

'''


'''
sample input : 
9
10 20 30 10 20 40 20 10 20

output:
3
'''
#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    unique_array = set(ar)
    each_pair_count = 0
    for element in unique_array:
        element_count = ar.count(element)
        each_pair_count += (element_count/2)
    return each_pair_count
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
