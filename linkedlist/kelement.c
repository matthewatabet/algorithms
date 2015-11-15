/*
 * Return the kth element from the end of a singly linked list.
 */

#include <stdlib.h>
#include <stdio.h>

struct node {
	struct node *next;
	int value;
};


struct list {
	struct node *head;
	struct node *tail;
};


struct list* list_new() {
	struct list *l = (struct list *) malloc(sizeof(struct list));
	l -> head = NULL;
	l -> tail = NULL;
	return l;
}


void list_add(struct list *l, int val) {

	// create new node
	struct node *n = (struct node *) malloc(sizeof(struct node));
	n -> value = val;
	n -> next = NULL;

	// ensure head
	if ( l -> head == NULL ) {
		l -> head = n;
	}

	// add to end
	if ( l -> tail == NULL ) {
		l -> tail = n;
	}

	else {
		l -> tail -> next = n;
		l -> tail = n;
	}

}


int nkelement(struct node *n, int k, int *i) {

	int ret = NULL;

	// base case, end of list.
	if (NULL == n -> next) *i = 0;

	// recurse
	else {
		ret = nkelement(n -> next, k, i);
		*i += 1;
	}

	if (k == *i) return n -> value;
	return ret;
}


int kelement(struct list *l, int k) {
	int i;
	return nkelement(l -> head, k, &i);
}


int main() {
	struct list * l = list_new();
	list_add(l, 5);
	list_add(l, 3);
	list_add(l, 7);
	printf("%d\n", kelement(l, 0));
	printf("%d\n", kelement(l, 1));
	printf("%d\n", kelement(l, 2));
	return 0;
}
