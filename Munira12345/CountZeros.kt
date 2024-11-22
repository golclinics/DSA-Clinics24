fun reverseInteger(input: Int): Int {
    // fixing Handling negative numbers
    val sign = if (input < 0) -1 else 1
    val reversedString = input.toString().removePrefix("-").reversed()
    return sign * reversedString.toInt()
}

fun main() {
    // Testing the inputs 500, -56, -90 and 91
    val testInputs = listOf(500, -56, -90, 91)

    for (input in testInputs) {
        val result = reverseInteger(input)
        println("Input: $input, Reversed: $result")
    }
}
