#include <stdio.h>
#include <unistd.h>
/**
 * main - PID
 * Return: 0 success
 */
int main(void)
{
	pid_t my_pid;

	my_pid = getpid();
	printf("%u\n", my_pid);
	return (0);
	return (0);
}
