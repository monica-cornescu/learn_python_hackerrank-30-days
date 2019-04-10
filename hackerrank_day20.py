'''
Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above.
Once sorted, print the following 3 lines:

Array is sorted in numSwaps swaps. where numSwaps is the number of swaps that took place.
First Element: firstElement where firstElement is the first element in the sorted array.
Last Element: lastElement where lastElement is the last element in the sorted array.
'''

import sys

n = int(input("n = ").strip())
a = list(map(int, input("List's elements are: ").strip().split(' ')))

numSwaps = 0
numSwaps_per_traversal = 0

# the list might not be sorted after only 1 traversal, so max n traversals might be needed, each with a number of swaps
for e in range(len(a)):
    numSwaps = numSwaps + numSwaps_per_traversal
    # reinitialize numSwaps_per_traversal, for each list traversal
    numSwaps_per_traversal = 0
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            swap = a[i]
            a[i] = a[i+1]
            a[i+1] = swap
            numSwaps_per_traversal = numSwaps_per_traversal + 1

print("Array is sorted in %d swaps" % numSwaps)
print("First Element: %d" % a[0])
print("Last Element: %d" % (a[len(a) - 1]))





