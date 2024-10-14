namespace WinnieNgina;

public class ReverseInterger
{
    public int ReverseInt(int num)
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
}
