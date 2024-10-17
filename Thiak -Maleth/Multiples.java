/* 
Write a program that prints the numbers from 1 to 100. 
For multiples of 3, print Fizz; for multiples of 5, print Buzz; 
and for numbers that are multiples of both 3 and 5, print FizzBuzz.
*/

public class Multiples {

    public static void multiples() {
        for (int i = 1; i <= 100; i++){
            if (i%3 == 0 && i%5 == 0) {
                System.out.println("FizzBuzz");
            }
            else if (i%3 == 0) {
                System.out.println("Fizz");
            } else if (i%5 == 0){
                System.out.println("Fuzz");
           } else {
            System.out.println(i);
           }
        }
    }

    public static void main(String[] args) {
        multiples();
    }
}