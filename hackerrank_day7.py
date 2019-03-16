#Given an array, , of integers, print 's elements in reverse order as a single line of space-separated numbers.

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

reverseArr = arr[::-1]
for elem in reverseArr:
    print(elem, "", end ="")

'''
or the for could be written as:
for i in range(len(reverseArr):
    print(reverseArr[i], "", end = "")
'''