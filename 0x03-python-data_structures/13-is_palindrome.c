#include "lists.h"
#include <stdlib.h>


/**
 * reverse_array - array to reverse
 * @a: int array
 * @n: array number of element
 * Return: concat strings
 */

void reverse_array(int *a, int n)
{
	int *begin = a;
	int *end;
	int hold = 0;

	end = a + n - 1;
	for (; begin < end; begin++, end--)
	{
		hold = *end;
		*end = *begin;
		*begin = hold;
	}
}
/**
 * is_palindrome - return 1 or 0
 * @head: linked list
 * Return: Return 1  if palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	int size, *list, *rev;
	listint_t *listcp = *head;

	if (!head || !listcp)
		return (0);
	if (!listcp->next)
		return (1);

	list = malloc(sizeof(int *));
	if (!list)
		return (0);
	rev = malloc(sizeof(int *));
	if (!rev)
		return (0);
	for (size = 0; listcp; listcp = listcp->next, size++)
		list[size] = listcp->n;

	list = rev;
	reverse_array(rev, size);
	if (list == rev)
		return (1);
	return (0);
}
