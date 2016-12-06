#
# Problem 6: Sum square difference
#
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
#
#
# Solution: 25164150
#
#


def sum_of_squares(upper_bound):

    sum_squares = 0
    for x in range(1, upper_bound + 1):
        sum_squares += x**2

    return sum_squares


def square_of_sums(upper_bound):
    square_sums = sum(range(1, upper_bound + 1))
    return square_sums**2


nums = 100
result = square_of_sums(nums) - sum_of_squares(nums)
print(result)
