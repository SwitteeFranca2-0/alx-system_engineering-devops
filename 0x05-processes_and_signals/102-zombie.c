#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - infinite while.
 * Return: int.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - main.
 * Return: int
 */
int main(void)
{
	char num = 0;
	pid_t zombie;

	for (num = 0; num < 5; num++)
	{
		zombie = fork();
		if (zombie > 0)
		{
			printf("Zombie process created, PID: %i\n", zombie);
			sleep(2);
		}
		else
		{
			exit;
		}

	}

	infinite_while();
	return (0);
}
