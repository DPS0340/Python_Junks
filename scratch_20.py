import math

prime = []
for i in range(1, 101):
    isprime = True
    for p in range(2, int(math.sqrt(i)) + 1):
        if i % p == 0:
            isprime = False
            break
    if isprime:
        prime.append(i)
print(prime)