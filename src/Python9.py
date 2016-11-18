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
# Solution: 31875000
#


import math


# iterate through a and b to find triplets. if the square of the sum of a + b is a
# natural number then the triplet is Pythagorean. Find the sum that equals 1000.
def prime_triplets_product(ubound):

    for a in range(1, ubound):
        for b in range(a + 1, ubound):
            c = math.sqrt(a * a + b * b)
            if c % 1 == 0:
                if a + b + c == 1000:
                    return a * b * int(c)

    return 0

print(prime_triplets_product(380))
