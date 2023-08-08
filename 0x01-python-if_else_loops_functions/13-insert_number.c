#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number in a sorted list
 * @head: the pointer to the given list
 * @number: the number to be inserted
 *
 * Return: the pointer to the list or NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
        listint_t *index;
	    listint_t *n_node;

	    n_node = malloc(sizeof(listint_t));
	    if (n_node == NULL)
		    return (NULL);
	    index = *head;
	    if (*head == NULL)
	    {
		    n_node = add_nodeint_end(head, number);
		    return (n_node);
	    }
	    if (number < index->n)
	    {
		    n_node->next = index;
		    n_node->n = number;
		    *head = n_node;
		    return (n_node);
	    }
	    while (index->next)
	    {
		    if (number < index->next->n)
		    {
			    n_node->next = index->next;
			    index->next = n_node;
			    n_node->n = number;
			    return (n_node);
		    }
		    index = index->next;
	    }
	    n_node = add_nodeint_end(head, number);
	    return (n_node);
}
