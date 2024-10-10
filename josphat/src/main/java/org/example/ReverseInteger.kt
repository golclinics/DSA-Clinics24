package org.example

/**
 * Solving the Entry Challenge C1 using Kotlin
 * Reverse Integer
 * Write a program that takes an integer as input and return an integer with reversed digit
 * ordering.
 *
 * For example
 *
 * For input 500, the program should return 5.
 * For input -56, the program should return -65.
 * For input -90, the program should return -9.
 * For input 91, the program should return 19.
 *
 */


/**
 * Todo: Reverses the digits of an integer using a recursive approach.
 *
 * @param input The integer to be reversed.
 * @return The integer with reversed digits.
 */
fun reverseIntegerRecursive(input: Int): Int {
    // Helper function that performs the recursive reversal
    // num: the remaining number to process
    // result: the current reversed result
    fun helper(num: Int, result: Int): Int {
        // Base case: when num is reduced to 0, return the accumulated result
        if (num == 0) return result
        // Recursive case: extract the last digit and add it to the reversed result
        return helper(num / 10, result * 10 + num % 10)
    }

    // Todo: Determine the sign of the input (1 for positive, -1 for negative)
    val sign = if (input < 0) -1 else 1
    // Call the helper function with the absolute value of the input
    // This ensures the recursion only deals with positive numbers
    val reversed = helper(input * sign, 0)
    // Restore the sign to the reversed result and return it
    return reversed * sign
}

fun main() {
    //Todo:  Testing the reverseIntegerRecursive function with various inputs
    println(reverseIntegerRecursive(500))    // Output: 5
    println(reverseIntegerRecursive(-56))    // Output: -65
    println(reverseIntegerRecursive(-90))    // Output: -9
    println(reverseIntegerRecursive(91))     // Output: 19
    println(reverseIntegerRecursive(1000))   // Output: 1
    println(reverseIntegerRecursive(-1000))   // Output: -1
    println(reverseIntegerRecursive(123456))  // Output: 54321
    println(reverseIntegerRecursive(-123456)) // Output: -54321
    println(reverseIntegerRecursive(100))    // Output: 1
    println(reverseIntegerRecursive(-100))   // Output: -1

}
