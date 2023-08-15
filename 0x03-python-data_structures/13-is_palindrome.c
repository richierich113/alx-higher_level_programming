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
		return (1);

	listint_t *slow = *head, *fast = *head;
	listint_t *prev = NULL, *temp;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	if (fast != NULL)
	slow = slow->next;

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
		return (0);

		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}
