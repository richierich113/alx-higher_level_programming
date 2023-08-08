#include "lists.h"

/**
 * check_cycle - checks if cycle exists or not a given linked list
 * list: linked list parameter
 * Return: 1 if cycle exists or 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *cur = list->next;
	listint_t *pst_cur = cur->next;

	if (cur != NULL && pst_cur != NULL)
		return (1);
	else
		return (0);
}
