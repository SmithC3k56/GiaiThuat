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
if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print("result: ",result)

