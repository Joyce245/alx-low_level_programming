#include <stdio.h>
#include <ctype.h>
/** 
* main - program that prints the alphabet 
* You can only use the putchar 
* Return: 0 
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
