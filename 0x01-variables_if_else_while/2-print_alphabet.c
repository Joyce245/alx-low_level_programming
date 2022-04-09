#include <stdio.h>
#include <ctype.h>
/**
* main - Entry point
* * Return: 0
*/
int main(void)
{
	int i = 'a';
while (i <= 'z')
{
putchar(i);
i += 1;
}
putchar('\n');
return (0);
}
