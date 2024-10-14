using WinnieNgina;

ReverseInterger reverseInterger = new ReverseInterger();
int value = 500;
int result = reverseInterger.ReverseInt(value);
Console.WriteLine(result);

FizzBuzz fizzBuzz = new FizzBuzz();
fizzBuzz.FizzBuzzImpl();

PowerOfTwo powerOfTwo = new PowerOfTwo();
int number = 10;
bool res = powerOfTwo.IsPowerOfTwo(number);
Console.WriteLine($"{number} => {res}");