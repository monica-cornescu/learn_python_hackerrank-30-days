#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input('Please provie a number between 2 and 20 and you\'ll get its multiples till 10: '))

for i in range(1,11):
    multiple = n * i
    print('%d x %d = %d' % (n, i, multiple))