/*  
    Name: Price Howard
    Student ID: 00652324
    Email: phoward1@una.edu
    Course Information: <CIS 315-02>
    Program Source File Name:  <GuessingGame.java>
    Programming Assignment:  #3 
    Program Description: The program is a game that the user guesses a random number and the game will tell if its higher or lower until the user guesses the number.
    References: N/A
    Due Date: 11/11/2020 	 
 
   In keeping with the honor code policies of the University of University of North Alabama, the School of Business, and the Department of Computer Science, I affirm that I have neither given nor received on this programming assignment. This assignment
represents my individual, original effort.
 ... My Signature is on File.
         
*/ 

import java.util.Random;
import java.util.Scanner;
public class GuessingGame {

	public static void main(String[] args) {
		int counter = 0;
		Random random = new Random();
		Scanner userInput = new Scanner(System.in);
		System.out.println("\tWelcome to the Guessing Game!");
		System.out.println("\t-----------------------------");
		System.out.println("I am thinking of a number between 1 and 20. Enter -1 if you would like to quit.");
		int numberToGuess = random.nextInt(20)+1;
		System.out.println("What is you guess? ");
		int guessedNumber = userInput.nextInt();
		while(guessedNumber != -1 && guessedNumber != numberToGuess)
		{
			if(guessedNumber > numberToGuess)
			{
				System.out.println("Your guess was to high try again.");
				counter++;
			}
			else
			{
				System.out.println("Your guess was to low try again.");
				counter++;
			}
			guessedNumber = userInput.nextInt();
		}
		if(guessedNumber == -1)
		{
			System.out.println("The number was: " + numberToGuess);
			System.out.println("The number of tries: " + counter);
			System.out.println("Okay, game over! Have a great day!");
		}
		else if(guessedNumber == numberToGuess)
		{
			System.out.println("Congrats! You nailed it!");
			System.out.println("The number of tries: " + counter);
			System.out.println("Okay, game over! Have a great day!");
		}
	}

}

