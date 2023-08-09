#include "lists.h"

/**
 * insert_node - inserts a node in a sorted singly linked list.
 * @head: head of node double pointer parameter
 * @number: int data to be inserted at new node
 * Return: address of new node or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;

	tmp = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (tmp->next != NULL)
	{
		if ((tmp->next)->n >= number)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	tmp->next = new;
	new->next = NULL;
	return (new);
}
