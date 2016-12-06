# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# Solution: 142913828922
#


# Build prime list with SOE below upper_bound and add them
def sum_of_primes_below(upper_bound):

    psum = 0
    prime_bools = sieve_of_eratosthenes(upper_bound)
    for n in range(0, len(prime_bools)):
        if prime_bools[n]:
            psum += n

    return psum


# Standard SOE
def sieve_of_eratosthenes(num_candidates):

    prime_bool_list = [True] * num_candidates
    prime_bool_list[0] = False
    prime_bool_list[1] = False

    for i in range(2, num_candidates):
        if prime_bool_list[i]:
            for j in range(i * i, num_candidates, i):
                prime_bool_list[j] = False

    return prime_bool_list


print(sum_of_primes_below(2000000))
