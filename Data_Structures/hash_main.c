#include <stdio.h>
#include <stdlib.h>
#include "hash.h"
/**
 * main - prints out the index return
 * Return: 0 success
 */
int main(void)
{
	char str1[100];
	unsigned long hash1;

	/*get input from user*/
	printf("Enter the string to store in the hash table: ");
	scanf("%99s", str1);

	hash1 = hash_function(str1);
	printf("Hash value of str1 is: %lu\n", hash1);

	return (0);
}
