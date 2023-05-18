#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    max_sum = float('-inf')  # Khởi tạo giá trị max_sum là giá trị âm vô cùng
    #Tính giá trị theo hình đồng hồ cát 
    for i in range(len(arr) - 2):  # Duyệt qua các hàng
        for j in range(len(arr) - 2):  # Duyệt qua các cột
            current_sum = (
                arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + # 3 phần tử bên trên
                arr[i + 1][j + 1] + # Phần tử ở giữa
                arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2] #3 phần từ ở dưới
            )
            max_sum = max(max_sum, current_sum)  # Cập nhật giá trị max_sum

    return max_sum

def hourglass_sum(arr):
    n = len(arr)
    m = len(arr[0])
    sums = [[0] * m for _ in range(n)]

    # Tính tổng các giá trị từ góc trái trên đến vị trí hiện tại
    for i in range(n):
        for j in range(m):
            sums[i][j] = arr[i][j] + (
                sums[i-1][j] if i > 0 else 0) + (
                sums[i][j-1] if j > 0 else 0) - (
                sums[i-1][j-1] if i > 0 and j > 0 else 0)

    max_sum = float('-inf')

    # Duyệt qua từng vị trí và tính tổng hourglass
    for i in range(2, n):
        for j in range(2, m):
            hourglass_sum = sums[i][j] - sums[i-2][j] - sums[i][j-2] + sums[i-2][j-2]
            max_sum = max(max_sum, hourglass_sum)

    return max_sum

if __name__ == '__main__':
    arr = []
    #Example for input:
    # 1 1 1 0 0 0
    # 0 1 0 0 0 0
    # 1 1 1 0 0 0
    # 0 0 2 4 4 0
    # 0 0 0 2 0 0
    # 0 0 1 2 4 0
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # result = hourglassSum(arr)
    result = hourglass_sum(arr)
    print("result: ",result)

