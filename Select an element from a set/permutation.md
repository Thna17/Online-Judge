**Select an element from a set**

---

## Description

This program calculates the number of cases in which selected elements are listed considering their order. The formula used is perm(n, r) = n × (n−1)×...×(n−r+1), where n represents the total number of elements in the set and r represents the number of elements to be selected.

For nonnegative integers n and r, it prints the value of perm(n, r) where n≥r.

---

## Concept Explanation

The task involves selecting r elements from a set of n elements, considering their order. The concept of permutations is used to calculate the number of such arrangements. Permutations deal with the arrangement of objects where the order matters.

The formula for permutations is:

\[ \text{perm}(n, r) = n × (n−1)×...×(n−r+1) \]

This formula calculates the number of ways to arrange r elements out of n distinct objects without repetition, where order matters.

---

## Code Explanation

- The function `permutation(n, r)` calculates the permutation using the provided formula.
- It first checks if \( r \) is greater than \( n \). If so, it returns 0 because permutation is not possible in such cases.
- It then iterates through \( r \) to calculate the product of consecutive decreasing numbers from \( n \) down to \( n-r+1 \).
- The main program takes input for \( n \) and \( r \), calculates the permutation using the function, and prints the result.

---

## Sample Input 1 

77 11

## Sample Output 1

266711567621704128000