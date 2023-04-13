#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
/**
 * main - use of execve
 * Return: 0 success
 */
int main(void)
{
	char *path = getenv("PATH");
	char *argv[] = {"/bin/ls", "-l", "/usr/", NULL};
	char *envp[] = {path, NULL};
	/**
	 * first str is the path of the ls command
	 * The other 2 strs are CL arguments of ls cmd
	 * Null indicates end of the arrays of strings
	 */
	printf("Before execve\n");
	if (execve(argv[0], argv, envp) == -1)
	{
		perror("Error:");
		/**
		 * 1st arg is the path to the ls cmd
		 * 2nd arg is the CL args of ls cmd
		 * 3rd arg is the new environ for new process
		 */
	}
	printf("After execve\n");
	return (0);
}
