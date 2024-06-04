def primeNumber(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def solve(n, m):
    for i in range(n , m + 1):
        if primeNumber(i):
            print(i)
n, m = map(int, input().split())
solve(n, m)