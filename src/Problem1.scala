
/*
 * Problem 1:
 *
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
 *
 * The sum of these multiples is 23.
 *
 * Find the sum of all the multiples of 3 or 5 below 1000.
 *
 * Solution: 233168
 */

import scala.collection.mutable.ArrayBuffer

object Problem1 {

    def main(args: Array[String]) {
        val mults = getMultsBelow(3, 5, 1000)
        println(mults.sum)
    }

    def getMultsBelow(multA: Int, multB: Int, max: Int): ArrayBuffer[Int] = {
        var mults = ArrayBuffer[Int]()

        for (x <- 1 until max) {
            if (x % multA == 0 || x % multB == 0) {
                mults += x
            }
        }
        mults
    }
}