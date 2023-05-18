#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def dynamicArray(n, queries):
    seqList = [[] for _ in range(n)]  # Tạo danh sách các dãy con rỗng
    lastAnswer = 0  # Khởi tạo giá trị lastAnswer ban đầu
    result = []  # Danh sách kết quả

    for query in queries:
        q, x, y = query

        if q == 1:  # Nếu là truy vấn 1
            seq = (x ^ lastAnswer) % n  # Xác định dãy con
            seqList[seq].append(y)  # Thêm y vào dãy con

        elif q == 2:  # Nếu là truy vấn 2
            seq = (x ^ lastAnswer) % n  # Xác định dãy con
            size = len(seqList[seq])  # Kích thước dãy con
            index = y % size  # Xác định vị trí trong dãy con
            lastAnswer = seqList[seq][index]  # Gán lastAnswer
            # Thêm lastAnswer vào danh sách kết quả
            result.append(lastAnswer)

    print('seq 1:',seqList[0])
    print('seq 2:',seqList[1])
    return result


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print('result: ', result)
