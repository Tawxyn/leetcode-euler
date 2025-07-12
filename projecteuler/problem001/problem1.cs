using System;
					
public class Program
{
	public static void Main()
	{
		int sum = 0;
		
		for (int i = 0; i < 1000; i++)
		{
			if (i % 3 == 0)
			{
				sum += i;
			}
			else if (i % 5 == 0)
			{
				sum += i;
			}
		}
		Console.WriteLine(sum);	
	}
}
