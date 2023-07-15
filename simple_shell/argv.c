#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
/**
 * main - prints all arguments without using ac
 * @ac: numbers of arguments
 * @av: arrays of strings (arguments)
 * Return: 0 success
 */
int main(int ac, char **av)
{
	char **arg; /*this a variable set*/

	arg = av;
	while (*arg)
	{
		printf("%s\n", *arg);
		arg++;
	}
	return (0);
}
