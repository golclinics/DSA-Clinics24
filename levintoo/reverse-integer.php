<?php
/*
 * Write a program that takes an integer as input and return an integer with reversed digit ordering.
 * 
 * Example inputs and expected outputs:
 * Input: 500  -> Output: 5
 * Input: -56  -> Output: -65
 * Input: -90  -> Output: -9
 * Input: 91   -> Output: 19
 */

function reverseInteger(int $num): int {
    $isNegative = $num < 0;

    $reversedString = strrev((string) abs($num));

    $reversedNumber = (int) $reversedString;

    return $isNegative ? -$reversedNumber : $reversedNumber;
}

// Test cases
echo reverseInteger(500) . "\n"; // Output: 5
echo reverseInteger(-56) . "\n"; // Output: -65
echo reverseInteger(-90) . "\n"; // Output: -9
echo reverseInteger(91) . "\n"; // Output: 19

?>
