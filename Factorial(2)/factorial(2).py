def fac(n):
    fac = 1
    calculate_process = ""
    for i in range(1, n + 1):
        fac *= i
        calculate_process += str(i)
        if i != n:
            calculate_process += "*"
    print(f"{n}!=({calculate_process})={fac}")
N = int(input())
fac(N)