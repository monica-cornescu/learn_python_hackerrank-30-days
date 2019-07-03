# Read a string, S, and print its integer value; if S cannot be converted to an integer, print Bad String.
#You must use the String-to-Integer and exception handling constructs

S = input().strip()

try:
    print(int(S))
except ValueError:
    print("Bad String")
