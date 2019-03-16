def factorial (n):
    fact = 1
    for x in range(2, n+1):
        fact = x * fact
    return fact


# or with recursion
def factorial_recursive (n):
    if n == 1:
        return 1
    elif n <= 0:
        return 0
    else:
        return factorial_recursive(n-1) * n


n = int(input("n = "))

print("factorial de %d = %d " % (n, factorial_recursive(n)))
