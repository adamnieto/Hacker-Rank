def isPrime(n):
    if n < 2:
        return "Not prime"
    elif n == 2:
        return "Prime"
    elif n % 2 == 0:
        return "Not prime"
    elif n == 3:
        return "Prime"
    else:
        i = 3
        while i*i <= n:
            if n % i == 0:
                return "Not prime"
            i += 2
        return "Prime"
#Get expected number of input
p = int(input().strip())
for i in range(p):
    n = int(input().strip())
    print(isPrime(n))
