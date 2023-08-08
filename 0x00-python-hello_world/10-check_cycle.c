#include "lists.h"

/**
 * check_cycle - checks if cycle exists or not a given linked list
 * list: linked list parameter
 * Return: 1 if cycle exists or 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *start, *fin;

	if (!list || !list->next)
	{
		return (0);
	}
	
	start = list;
	fin = list;
	
	while (fin != NULL && start->next != NULL && start->next->next != NULL)
	{
		start = start->next->next;
		fin = fin->next;

		if (start == fin)
		{
			return (1);
		}
	}
	return (0);
}
