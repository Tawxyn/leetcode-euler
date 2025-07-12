using System;
					
public class Program
{
	public static void Main()
	{
		int a = 1;
        int b = 2;
        int sum = 0;

        while (b <= 4000000)
        {
            if (b % 2 == 0)
            {
                sum += b;
            }

            int next = a + b;
            a = b;
            b = next;
        }

        Console.WriteLine(sum);
	}
}
