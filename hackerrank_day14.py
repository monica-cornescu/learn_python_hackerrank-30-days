'''Today we're discussing scope.
The absolute difference between two integers, a and b, is written as |a-b| . The maximum absolute difference between
two integers in a set of positive integers, elements, is the largest absolute difference between any two integers in.
The Difference class is started for you in the editor. It has a private integer array (elements) for storing
non-negative integers, and a public integer (maximumDifference) for storing the maximum absolute difference.
Task
Complete the Difference class by writing the following:
A class constructor that takes an array of integers as a parameter and saves it to the elements instance variable.
A computeDifference method that finds the maximum absolute difference between any 2 numbers in N and stores it in the
maximumDifference instance variable.
'''


class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        maximumDifference = max(a) - min(a)


#_ = input()
#a = [int(e) for e in input().split(' ')]
a = [100, 72, 4, 39, 1234, 15, 28]
d = Difference(a)
print(d.computeDifference())

print(d.maximumDifference)
