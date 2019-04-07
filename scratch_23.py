import math

prime = []
for i in range(1, 1001):
    isprime = True
    for p in range(2, int(math.sqrt(i)) + 1):
        if i % p == 0:
            isprime = False
            break
    if isprime and i > 2 and (i % 10) == 1:
        prime.append(i)
print(prime)
