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

def reverseArray(a): # gọi là slicing 
    # Write your code here
    """
    sử dụng hàm slicing để đảo ngược mảng
    :: lấy hết các phần tử trong mảng
    -1 là bước nhảy-> mảng sẽ cắt từng phần tử từ phần tử cuối cùng có index -1 cho đến hết
    """
    return a[::-1]
def reverse_array2(arr): # cách này là dùng vòng lặp
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

def reverse_array(arr):# Dùng đệ quy
    if len(arr) <= 1:
        return arr
    return reverse_array(arr[1:]) + [arr[0]]


if __name__ == '__main__':
    
    #Ví dụ cho input:
    #5
    #1 2 3 4 5
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    # res = reverse_array2(arr)
    res = reverse_array(arr)
    # res = reverseArray(arr)
    print("result: ",res)

    