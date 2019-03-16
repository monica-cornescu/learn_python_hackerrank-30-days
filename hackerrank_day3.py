import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())

oddness = N % 2
if oddness == 1:
    print('Weird')
elif oddness == 0 and 2 <= N <= 5:
    print("Not weird")
elif oddness == 0 and 6 <= N <= 20:
    print('Weird')
elif oddness ==0 and N > 20:
    print('Not Weird')