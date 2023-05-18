#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here
    """
    sử dụng hàm slicing để đảo ngược mảng
    :: lấy hết các phần tử trong mảng
    -1 là bước nhảy-> mảng sẽ cắt từng phần tử từ phần tử cuối cùng có index -1 cho đến hết
    """
    return a[::-1]

if __name__ == '__main__':
    

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)
    print("result: ",res)

    