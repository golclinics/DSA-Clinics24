/* Write a program that takes an integer as input and return an integer with reversed digit
ordering.

For example

For input 500, the program should return 5. 
For input -56, the program should return -65. 
For input -90, the program should return -9. 
For input 91, the program should return 19.  */

import java.util.Scanner;
public class ReverseInt{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter an integer: ");
        int inum = sc.nextInt();
        int reversed = reverseDigit(inum);
        System.err.println("Reversed integer: " + reversed);
    }
    public static int reverseDigit(int num){
        int reversed =0;
        int var;
        while(num!=0){
            var =  num % 10;
            reversed = reversed * 10 + var;
            num /= 10;
        }
        return reversed;
    }
}