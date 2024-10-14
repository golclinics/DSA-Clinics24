namespace WinnieNgina;

public class PowerOfTwo
{
    public bool IsPowerOfTwo(int num)
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
}
