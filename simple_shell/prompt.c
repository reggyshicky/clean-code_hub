#include <stdio.h>
#include <string.h>
/**
 * main - prints $ and waits user to enter a cmd and prints it to newline
 * Return: 0 success
 */
int main(void)
{
	char command[100];

	while (1) /*unending loop, while true*/
	{
		printf("$ ");
		fgets(command, 100, stdin);
		/**
		 * 100 tells fgets to read atmost 100 characters
		 * stdin tells we're reading from the console
		 * fgets reads user's input from console
		 */
		command[strcspn(command, "\n")] = '\0';
		/**
		 * this line removes the newline character that is
		 * addeed to end of the command by fgets by replacing it
		 * with a nulll character
		 * the strcspn returns new length of the initial segment of str
		 * command that does not contain \n
		 */
		if (strcmp(command, "exit") == 0)
		{
			break;
			/**
			 * checks if the command entered is equal to the str
			 * "exit", if its break is used to exit the loop
			 */
		}
		printf("%s\n", command);
	}
	return (0);
}
