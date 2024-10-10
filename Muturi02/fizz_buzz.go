package main
import "fmt"
func main(){
	for i:=1;i<= 100;i++{
		if i%3==0 && i%5==0{//check this condition first. Output will be different if it is checked last. No "FizzBuzz" will be printed
			fmt.Print("FizzBuzz\n")
		}else if i %3==0{
			fmt.Print("Fizz\t")
		}else if i%5==0{
			fmt.Print("Buzz\t")
		}else{
			fmt.Print(i,"\t")
		}
	}
	fmt.Println()
}