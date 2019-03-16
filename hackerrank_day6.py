'''Given a string, , of length that is indexed from to , print its even-indexed and odd-indexed characters as
space-separated strings on a single line (see the Sample below for more detail).
Note: is considered to be an even index.
'''

t = int(input())
for i in range(t):
    S = str(input())
    Slength = len(S)
    S_odd = ''
    S_even =''

    for j in range(Slength):
        if (j == 0) or (j % 2 == 0):
            S_even = S_even + S[j]
        else:
            S_odd = S_odd + S[j]
    print(S_even, S_odd)