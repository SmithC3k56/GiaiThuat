#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr): # basic 1
    # Write your code here
    new_arr = []
    for i in range(len(arr)):
      if i+d < len(arr):
       new_arr.append(arr[i+d])
      else:
       new_arr.append(arr[(i+d) % len(arr)])
    return new_arr

def rotateLeft2(k, arr): # tách mảng thành 2 phần (1 là từ index k -> hêt, 2 là phần còn lại )
    n = len(arr)
    k = k % n

    temp = arr[k:] + arr[:k]
    arr[:] = temp

    return arr
def rotateLeft3(k, arr):# cách nổi bọt 
    n = len(arr)
    k = k % n

    for _ in range(k):
        temp = arr[0]
        for i in range(n-1):
            arr[i] = arr[i+1]
        arr[n-1] = temp

    return arr

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft3(d, arr)
    print('result',result)
