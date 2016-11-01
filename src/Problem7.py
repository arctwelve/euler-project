# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10,001st prime number?
#
# Solution: 104743
#
import math


# Standard Sieve of Eratosthenes
def prime_sieve(amt):

    prime_bool_list = [True] * amt
    prime_bool_list[0] = prime_bool_list[1] = False

    for i in range(2, math.floor(math.sqrt(amt))):
        if prime_bool_list[i]:
            for j in range(i * i, amt, i):
                prime_bool_list[j] = False

    return prime_bool_list


# Actual prime storage
def store_primes(bool_list):
    real_primes = []
    for i in range(0, len(bool_list)):
        if bool_list[i]:
            real_primes.append(i)

    return real_primes


candidates = 104750
bool_primes = prime_sieve(candidates)
primes = store_primes(bool_primes)

print(primes[10000])
