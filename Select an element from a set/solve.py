def permutation(n, r):
    if r > n:
        return 0
    perm = 1
    for i in range(r):
        perm *= (n - i)
    return perm
n, r = map(int, input().split())
print(permutation(n, r))