#include "lists.h"
/**
 * is_palindrome - function check if a lis if forming a palindrome
 * pattern
 * @head: head node of the list to be checked
 *
 * Return: returns 0 if it is not a palindrome otherwise return 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *curr = slow;
	listint_t *next = NULL;
	listint_t *left = *head;
	listint_t *right = prev;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	while (right != NULL)
	{
		if (left->n != right->n)
			return (0);
		left = left->next;
		right = right->next;
	}

	return (1);
}
