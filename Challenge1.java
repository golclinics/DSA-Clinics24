//Write a program that takes an integer as input and return an integer with reversed digit
//ordering.

import java.util.Scanner;

public class Challenge1{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an Integer : ");
        int myInt = scanner.nextInt();

        int reversed_number = reverse_integer(myInt);
        System.out.println("Reversed integer: " + reversed_number);

        scanner.close();
    }

    public static int reverse_integer(int myInt){
        int reversed_number = 0;
        while (myInt > 0){
            int lastDigit = myInt % 10;
            reversed_number = (reversed_number * 10) + lastDigit;
            myInt = myInt / 10;
        }
        return reversed_number;
    }
}