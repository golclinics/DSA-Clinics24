using System;

class Program
{
    static void Main()
    {
        // prompts the user to enter an integer
        Console.WriteLine("Enter an integer:");

        // read the input an try to parse it as integer
        if (int.TryParse(Console.ReadLine(), out int number))
        {
            // call the ReverseDigits method and output the result
            int reversedNumber = ReverseDigits(number);
            Console.WriteLine($"The reversed number is: {reversedNumber}");
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a valid integer.");
        }
    }

    static int ReverseDigits(int number)
    {
        // check is a number is negative
        bool isNegative = number < 0;

        // convert the number to its absolute value
        number = Math.Abs(number);

        // initialize the reversed number to 0
        int reversedNumber = 0;

        // extract each digit from the number and build the reversed number
        while (number > 0)
        {
            // get the last digit from the number.
            // for example id number is 46 then 46 % 10 is 6
            int digit = number % 10;
            // start assembling the reversed number
            reversedNumber = reversedNumber * 10 + digit;
            // remove the last digit of the number 
            number /= 10;
        }

        // retain the sign of the number
        return isNegative ? -reversedNumber : reversedNumber;
    }
}

