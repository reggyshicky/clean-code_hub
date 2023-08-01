#include <stdio.h>
#include <unistd.h>
/**
 * main - use of fork
 * Return: 0 success
 */
int main(void)
{
	pid_t my_pid;
	pid_t child_pid;

	child_pid = fork();
	if (child_pid == -1)
	{
		perror("Error:");
		return (1);
	}
	my_pid = getpid(); /*getting the pid for the current process*/
	printf("My pid is %u\n", my_pid);

	if (child_pid == 0)
	{
		printf("(%u) it is a child process\n", my_pid);
	}
	else
	{
		printf("%u) %u, I am your father\n", my_pid, child_pid);
	}
	return (0);
}
/* Using the return value of fork, it is possible to know*/
/*if the current process is the father or the child*/
/*fork will return 0 to the child, and the PID of the child to the father*/

