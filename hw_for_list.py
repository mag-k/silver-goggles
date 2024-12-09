numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for number in numbers:
    n = 0
    for j in range(1, number + 1):
        if number % j == 0:
           n += 1
    if n == 2:
        primes.append(number)
    elif n > 2:
        not_primes.append(number)

print(primes)
print(not_primes)
