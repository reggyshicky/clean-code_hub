#include <stdio.h>
#include <unistd.h>
/**
 * main - PID
 * Return: 0 success
 */
int main(void)
{
	/*pid_t is a data type found in unistd.h*/
	pid_t my_pid;

	my_pid = getpid();
	printf("%u\n", my_pid);
	return (0);
}
