#!/bin/python3

import math
import os
import random
import re
import sys


def getTotalX(a, b):
    lcm_a = a[0]
    gcd_b = b[0]

    # Tìm least common multiple (LCM) của mảng 'a'
    for i in range(1, len(a)):
        lcm_a = (lcm_a * a[i]) // math.gcd(lcm_a, a[i])

    # Tìm greatest common divisor (GCD) của mảng 'b'
    for i in range(1, len(b)):
        gcd_b = math.gcd(gcd_b, b[i])

    count = 0
    for x in range(lcm_a, gcd_b + 1, lcm_a):
        if gcd_b % x == 0:
            count += 1

    return count




if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
    print(total)

