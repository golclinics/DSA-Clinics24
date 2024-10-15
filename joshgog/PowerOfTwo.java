public class PowerOfTwo {
    public static boolean isPowerOfTwo(int n) {
        if (n <= 0) {
            return false;
        }
        return (n & (n - 1)) == 0;
    }

    public static void main(String[] args) {
        int number1 = 8;
        int number2 = 5;
        
        System.out.println(isPowerOfTwo(number1)); //  true
        System.out.println(isPowerOfTwo(number2)); //  false
    }
}
