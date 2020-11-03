

// Price Howard
// 10/27/2020
// CIS315
// Program takes user input into an array and then prints the minimum number,
// the maximum number, and the sum of all of the inputed numbers into the array.



import java.util.Scanner;
import java.lang.Math;
public class MinMaxArray
{

	
	public static void main (String [] args)
	{
		Scanner userInput = new Scanner(System.in);
		int []array = new int[5];
		for(int i=0; i<5; i++)
		{
			System.out.println("Enter integer number " + (i+1));
			array[i] = userInput.nextInt();
		}
		findMax(array);
		findMin(array);
		findSum(array);
		
	}
	
	/*
	 * Name: findMax
	 * Purpose: To find the max value in the array
	 * Return: N/A
	 */
	
	public static void findMax(int functArray[])
	{
		int max=0;
		for( int i = 0; i<5; i++)
		{
			if(functArray[i] > max)
			{
				max = functArray[i];
			}
		}
		System.out.println("The max value in the array is: " + max);
	}
	
	/*
	 * Name: findMin
	 * Purpose: To find the min value in the array
	 * Return: N/A
	 */
	
	public static void findMin(int functArray[])
	{
		int min=functArray[0];
		for( int i = 1; i<5; i++)
		{
			if(functArray[i] < min)
			{
				min = functArray[i];
			}
		}
		System.out.println("The min value in the array is: " + min);
	}
	
	/*
	 * Name: findSum
	 * Purpose: To find the sum of the array
	 * Return: N/A
	 */
	
	public static void findSum(int functArray[])
	{
		int Sum=0;
		for( int i = 0; i<5; i++)
		{
			Sum+=functArray[i];
		}
		System.out.println("The sum of the array is: " + Sum);
	}
}
