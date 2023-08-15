#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
  * is_palindrome -  checks if a singly linked list is a palindrome.
  * @head: head node of linked list
  * Return: 1 if palindrome, 0 otherwise
  */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	listint_t *one_step = *head;
	listint_t *two_steps = *head;

	while (two_steps != NULL && two_steps->next != NULL)
	{
		one_step = one_step->next;
		two_steps = two_steps->next->next;
	}

	one_step = reverse(one_step);
	two_steps = *head;

	while (one_step != NULL)
	{
		if (one_step->n != two_steps->n)
		{
			return (0); // Not a palindrome
		}
		one_step = one_step->next;
		two_steps = two_steps->next;
	}

	return (1);
}
