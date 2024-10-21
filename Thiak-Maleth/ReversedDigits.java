import java.util.Scanner;

public class ReversedDigits {

    public static int reversedDigits(int x) {
        int reversed = 0;
        while (x != 0) {
            int digit = x % 10;
            x /= 10;

            if (reversed > Integer.MAX_VALUE / 10 || (reversed == Integer.MAX_VALUE && digit > 7)) {
                return 0;
            }
            if (reversed < Integer.MIN_VALUE / 10 || (reversed == Integer.MIN_VALUE && digit < -8)) {
                return 0;
            }

            reversed = reversed * 10 + digit;
        }
        return reversed;
    }

    public static void main(String[] args) {
        //Scanner
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number: ");
        int input = scanner.nextInt();
        
        System.out.println("Reversed number: " + reversedDigits(input));

        scanner.close();
    }
}