To create a Markdown file with the program, its explanation, and a flowchart, let's organize the document as follows:

---

# Prime Number Finder Program

## Description

This program is designed to find and print all prime numbers within a given range from M to N.

---

## Input

The program takes input from the user in the following format:
```
M N
```
Where:
- M is the starting number (M ≤ N)
- N is the ending number (M ≤ N)

Only inputs with at least one prime number greater than or equal to M and less than or equal to N are accepted.

---

## Output

The program prints decimal numbers in increasing order, one per line.

---

## Algorithm

### `primeNumber` Function:
1. Iterate through numbers from 2 to n-1.
2. Check if n is divisible by any number in that range.
3. If n is divisible by any number, return False (indicating n is not prime).
4. If no divisor is found, return True (indicating n is prime).

### `solve` Function:
1. Iterate through numbers from n to m.
2. For each number in the range, check if it's prime using the `primeNumber` function.
3. If a number is prime, print it.

---



## Sample Usage

### Input:
```
12 24
```

### Output:
```
13
17
19
23
```

---