#include "lists.h"
/**
 * check_cycle - check if there is a cycle in a loop
 * @list: the linked list to be checked
 *
 * Return: Returns 0 if there no cycle or 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return (0);

	slow = list;
	fast = list;
	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
