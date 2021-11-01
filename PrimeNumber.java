import java.util.*;
class PrimeNumber
{
	public static void main(String[] args) 
	{
		int number = 3;
		boolean flag = false;
		for(int i=2; i<number-1; i++)
		{	
			flag = true;

		}

		if(flag == true)
		{
			System.out.println("Number is not prime:");
		}
		else
		{
			System.out.println("Number is prime:");
		}
	}
}