
/*
 * Problem 3:
 *
 * The prime factors of 13195 are 5, 7, 13 and 29.
 *
 * What is the largest prime factor of the number 600851475143 ?
 *
 * Solution:
 */
import scala.collection.mutable.ArrayBuffer


object Problem3 {


    def main(args: Array[String]) {
        val primeFactors:ArrayBuffer[Long] = getPrimeFactors(13195)
        println(primeFactors)
    }


    /*
     * Returns factors of num.
     */
    def getPrimeFactors(num:Long): ArrayBuffer[Long] = {

        val primes = getPrimesTo(num / 2)
        var factors = ArrayBuffer[Long]()

        for (p <- primes) {
            if (num % p == 0) factors += p
        }
        factors
    }


    /*
     * Returns primes up to and including n, if n is prime
     */
    def getPrimesTo(n:Long): ArrayBuffer[Long] = {
        var primes = ArrayBuffer[Long]()

        var possPrime:Long = 2
        while (possPrime <= n) {
            if (isPrime(possPrime)) primes += possPrime
            possPrime += 1
        }
        primes
    }


    /*
     * Takes a single Long and determines if it's prime
     */
    def isPrime(n:Long): Boolean = {

        // loop back from j at n - 1. If n is mod 0 by any j > 2 then n isn't prime
        for (j: Long <- (n - 1) to 2 by -1) {
            if (n % j == 0) return false
        }
        true
    }
}
