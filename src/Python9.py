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


import math


# iterate through a and b to find triplets. if the square of the sum of a + b is a
# natural number then the triplet is Pythagorean. Find the sum that equals 1000.
def build_prime_triplets(mxa):
    triplet = 0
    for a in range(1, mxa):
        for b in range(a + 1, mxa):
            c = math.sqrt(a * a + b * b)
            if c % 1 == 0:
                if a + b + c == 1000:
                    triplet = [a, b, int(c)]

    return triplet


print(build_prime_triplets(1000))
