#include <stdio.h>
#include <stdlib.h>
# define CAPACITY 200

/**
 * hash_function - function that calculates the index in a harshtable
 * @str: string to store in a hash table
 * Return: the index of the value
 */
unsigned long hash_function(char *str)
{
	unsigned long int i = 0; /*stores the sum of the Ascii values*/
	int j; /*counter of the string*/

	for (j = 0; str[j]; j++)
		i = i + str[j];
	return (i % CAPACITY);
}
