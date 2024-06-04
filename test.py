def permutation(n, r):
    """
    Calculate the permutation of n objects taken r at a time.
    
    Args:
        n (int): Total number of objects.
        r (int): Number of objects to be chosen.
        
    Returns:
        int: Permutation of n objects taken r at a time.
    """
    if r > n:
        return 0  # If r is greater than n, permutation is not possible
    
    perm = 1
    for i in range(r):
        perm *= (n - i)
    
    return perm

# Sample Input
n, r = map(int, input().split())

# Calculate permutation
permutation_value = permutation(n, r)

# Output the result
print(permutation_value)

