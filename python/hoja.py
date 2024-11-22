def isPrime(n):
    if n == 3 or n == 2:
        return True
    for i in range(2, n-1):
        if n % i != 0 or n == 2 or n == 3:
            return True
        else:
            return False
n = 7

print(isPrime(n))