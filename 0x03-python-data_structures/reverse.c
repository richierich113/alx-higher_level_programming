#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
  * reverse - reverse a linked list.
  * @head: head node of linked list to reverse
  * Return: reversed list
  */
listint_t *reverse(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return prev;
}
