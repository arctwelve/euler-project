# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10,001st prime number?
#
# Solution: 104759
#


primeSieve = []
primes = []


def is_prime(val):
    if val < 2:
        return False
    for i in range(2, val):
        if val % i == 0:
            return False

    return True


def sieve_primes(amount):

    for i in range(amount):
        primeSieve.append(0)

    for i in range(amount):
        if primeSieve[i] == 0 and is_prime(i):
            primeSieve[i] = 1
            primes.append(i)
            for x in range(i * 2, amount, i):
                primeSieve[x] = -1


candidates = 110000
sieve_primes(candidates)

print(primes[10001])
