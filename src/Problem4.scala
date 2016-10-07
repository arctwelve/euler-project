/*
 * Problem 4:
 *
 * A palindromic number reads the same both ways.
 *
 * The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 *
 * Find the largest palindrome made from the product of two 3-digit numbers.
 *
 * Solution: 906609
 */
object Problem4 {


    /*
     * Start with the largest three digit numbers and work backwards, decrementing one
     * of the two values in one loop and the other value in the next loop.
     */
    def main(args: Array[String]) {
        println(largestPalendromeProduct(999, 999))
    }


    /*
     * Second value is decremented each loop by 1. When that reaches 1 the first value
     * is decremented by 1 and the second value is reset to its original value.
     */
    def largestPalendromeProduct(a:Int, b:Int):Int = {

        var valA:Int = a
        var valB:Int = b
        var lastHighest:Int = 0

        while (valA > 0) {

            val product:Int = valA * valB
            if (isPalendrome(product)) {
                if (product > lastHighest) lastHighest = product
            }

            valB -= 1
            if (valB < 1) {
                valA -= 1
                valB = valA - 1
            }
        }
        lastHighest
    }


    /*
     * Simple string reversal comparison
     */
    def isPalendrome(n:Int):Boolean = {
        n.toString.reverse == n.toString
    }
}