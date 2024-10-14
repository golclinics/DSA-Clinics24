int value = 500;
int result = ReverseInt(value);
Console.WriteLine(result);
static int ReverseInt(int num)
{
    int value = num < 0 ? Math.Abs(num) : num;
    int result = 0;
    while (value > 0)
    {
        result = result * 10 + value % 10;
        value /= 10;
    }
    return num < 0 ? result * -1 : result;
}
static void FizzBuzz()
{
    for (int i = 1; i <= 100; i++)
    {
        if (i % 3 == 0 && i % 5 == 0)
        {
            Console.WriteLine("FizzBuzz");
        }
        else if (i % 3 == 0)
        {
            Console.WriteLine("Fizz");
        }
        else if ((i % 5) == 0)

        {
            Console.WriteLine("Buzz");
        }
        else
        {
            Console.WriteLine(i);
        }
    }
}
FizzBuzz();
static bool IsPowerOfTwo(int num)
{
    double value = 0;
    double i = 0;
    while (value <= num)
    {
        value = Math.Pow(2, i);
        i++;
        if (value == num)
        {
            return true;
        }
    }
    return false;
}
int number = 10;
bool res = IsPowerOfTwo(number);
Console.WriteLine($"{number} => {res}");