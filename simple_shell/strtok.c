#include <stdio.h>
#include <string.h>
/**
 * main - splits a string and returns an array of each word of str
 * Return: 0 success
 */
int main(void)
{
	char str[] = "I love solving problems in SE";
	char *token; /*strtok returns a ptr to the 1st token*/

	token = strtok(str, " ");
	/**
	 * strtok takes 2 args,a string to be tokenized and a delimiter
	 * a delimiter seperates tokens
	 */
	while (token != NULL)
	{
		printf("%s\n", token);
		token = strtok(NULL, " ");
		/**
		 * subsequen calls to strtok with a null pointer as the first
		 * arg will continue to rturn the next token in the str
		 */
	}
	return (0);
}
