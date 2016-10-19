/*
 * Problem 5
 *
 * 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 *
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 *
 * Solution: 232792560
 */
object Problem5 {


    /*
     * Start at the highest of the divisors as the smallest possible number, divide by each number decrementing
     */
    def main(args: Array[String]) {

        val start:Double = 20
        var upperBound: Double = start
        var smallestPossible:Double = start

        while (upperBound > 0) {
            val quotient:Double = smallestPossible / upperBound
            if (! isInt(quotient)) {
                smallestPossible += 1
                upperBound = start
            }
            upperBound -= 1
        }
        println(smallestPossible.toInt);
    }


    def isInt(value:Double):Boolean = {
        value % 1 == 0
    }
}
