#include <stdio.h>

void array_reverse()
{
	int array[] = {1, 2, 4, 5, 6};
	int i, j;
	int temp;
	int n = sizeof(array) / sizeof(array[0]);

	for (i = 0; i < (n/2); i++)
	{
		temp = array[i];
		array[i] = array[n - i - 1];
		array[n - i - 1] = temp;
	}
	for (j = 0; j < n; j++)
	{
		printf("%d\n", array[j]);
	}

}
int main ()
{
	array_reverse();
}
