
fun main() {
    print("Enter an integer: ")
    val n = readlnOrNull()?.toInt() ?: 0
    println(isPowerOfTwo(n))
}

fun isPowerOfTwo(n: Int): Boolean {
    return n > 0 && (n and (n - 1)) == 0
}