/*
 * Problem 3:
 *
 * The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number 600851475143 ?
 *
 * Solution: 6857
 */
import scala.collection.mutable.ArrayBuffer

/*
 * Divide the divident by the divisor -- if the result is an int, store it as a prime factor and set the new dividend
 * to the old quotient. If the result is not an int increment the divisor by 1. loop while the quotient is > 1
 */
object Problem3 {


    val targetNum:Double = 600851475143D
    var primeFactors: ArrayBuffer[Long] = ArrayBuffer[Long]()

    var dividend:Double = targetNum
    var divisor:Double = 2
    var quotient:Double = 2


    def main(args: Array[String]) {

        while (quotient > 1.0) {

            quotient = dividend / divisor

            if (isInt(quotient)) {
                primeFactors += divisor.toLong;
                dividend = quotient
            } else {
                divisor += 1
            }
        }
        println(primeFactors)
    }


    def isInt(value:Double):Boolean = {
        value % 1 == 0
    }
}
