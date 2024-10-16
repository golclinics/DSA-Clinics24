using System;

public class ReverseInteger
{
    public static int ReverseNumber(int number)
    {
        bool isNegative = number < 0;
        
        string numberString = Math.Abs(number).ToString();        
        char[] charArray = numberString.ToCharArray();
        Array.Reverse(charArray);
        
        int reversedNumber = int.Parse(new string(charArray));
        
        // Return the reversed number with the original sign
        return isNegative ? -reversedNumber : reversedNumber;
    }

    public static void Main(string[] args)
    {
        Console.WriteLine(ReverseNumber(500));  // Output: 5
        Console.WriteLine(ReverseNumber(-56));  // Output: -65
        Console.WriteLine(ReverseNumber(-90));  // Output: -9
        Console.WriteLine(ReverseNumber(91));  // Output: 19
    }
}