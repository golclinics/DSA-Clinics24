/* 
Write a program that prints the numbers from 1 to 100. 
For multiples of 3, print Fizz; for multiples of 5, print Buzz; 
and for numbers that are multiples of both 3 and 5, print FizzBuzz.
*/

public class Multiples {

    public static void multiples(int number) {
        for (int i = 0; i <= number; i++){
            if (i%3 == 0 && i%5 == 0) {
                System.out.println("FizzBuzz");
            }
            else if (i%3 == 0) {
                System.out.println("Fizz");
            } else if (i%5 == 0){
                System.out.println("Fuzz");
           } 
        }
    }

    public static void main(String[] args) {
        int number = 100;
        multiples(number);
    }
}

    public static void main(String[] args) {
        int number = 100;
        multiples(number);
    }
}