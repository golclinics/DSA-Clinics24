public class FizzBuzz{
    public static void main(String[] args) {
        printResponse();
    }
    public static void printResponse(){
        for (int i = 1; i < 101; i++) {

            if(i % 3 != 0 && i % 5 != 0){
                System.out.println(i);
            }
            else if(i % 3 == 0 && i % 5 != 0){
                System.out.println("Fizz");
            }

            else if(i % 3 != 0 && i % 5 == 0){
                System.out.println("Buzz");
            }

            else{
                System.out.println("FizzBuzz");
            }

        }
    }
}