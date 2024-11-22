using System;

class Program {
    static void Main(){
        for(int i = 1; i <=100; i++){
            if(i%3 == 0 && i%5 == 0){
                System.Console.WriteLine("Fizz buzz");
            }
           else if(i % 5 == 0){
                System.Console.WriteLine("Fizz");
            }
            else if(i%3 == 0){
                System.Console.WriteLine("Buzz");
            }
            else{
                System.Console.WriteLine(i);
            }
        }
    }
}