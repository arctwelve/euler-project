#
# Problem 9
#
# Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#
# Find the product abc.
#
# Solution:
#


# iterate through a and b to find triplets. see if the square of the sum is a natural number
import math


def build_prime_triplets(high_range):
    triplets = []
    for a in range(1, high_range):
        for b in range(a + 1, high_range):
            c = math.sqrt(a * a + b * b)
            if c % 1 == 0:
                triplet = [a, b, int(c)]
                triplets.append(triplet)

    return triplets


print(build_prime_triplets(20))
