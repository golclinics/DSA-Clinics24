using System;
class CheckPowerIFofTwo
{
    //Check the interger if is power of 2 
    static bool IfPowerOfTwo(int X)
    {
        return X > 0 && (X &(X-1)) == 0;
    }
    // Enter the interger
    static void Main()
    {
        Console.WriteLine("Enter the Number: ");
        int num;

        //Check if integer is power of two and return true or false
 if (int.TryParse(Console.ReadLine(), out num))
 {
        if (IfPowerOfTwo(num))
        {
            Console.WriteLine(true);
        }
        else
        {
            Console.WriteLine(false);
        }

    }
    }
}