#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

extern char **environ;

//extern is used to declare a variable or function that is defined in another source file or module
//environ is an external var defined in C stdlib, reps a pointer to an array of strings that contain the env variablws for the current process

int main(int argc, char **argv[])
{
	int i = 0;

	printf("\n");
	while (environ[i] != NULL)
	{
		printf("[%s] :: ", environ[i]);
		i++;
	}

	char *val = getenv("USER");
	//getenv retrieves the value of a specific environment var called "USER"
	printf("\n\nCurrent Value of environment variable USER  is [%s]\n", val);
	if (setenv("USER", "Reggy", 1))
	{
		printf("\n setenv() failed\n");
		return 1;
	}
	// setenv sets a new value to an environment variable
	// The if statement checks the return value of setenv. if setenv
	// fails to set the env var, it returns a non-zero value.
	printf("\n Succesfully added a new value to existing environment variable USER\n");
	val = getenv("USER");
	printf("\nNew value of environment variable USER is [%s]\n", val);

	while(1)
	{
		sleep(2);
	}
	return 0;
}
