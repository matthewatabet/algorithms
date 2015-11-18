/*
 * Remove duplicates from a linked list.
 */

#include <stdlib.h>
#include <stdio.h>


struct node {
	int v;
	struct node *n;
};


struct node *new_node(int v) {
	struct node *n = (struct node*) malloc(sizeof(*n));
	n -> v = v;
	n -> n = NULL;
	return n;
};


void print_list(struct node *n) {
	if (NULL == n) printf("\n");
	else {
		printf("%d ", n->v);
		print_list(n -> n);
	}
};

struct node *add(struct node *n, int v) {
	if ( NULL == n ) return new_node(v);
	else n->n = add(n->n, v);
	return n;
};


int contains(struct node *n, int v) {
	if (NULL == n) return 0;
	else if ( n->v == v ) return 1;
	else return contains(n->n, v);
};


struct node *remove_duplicates(struct node *n) {
	if ( NULL == n ) return NULL;
	n->n = remove_duplicates(n->n);
	if ( contains(n->n, n->v) ) {
		struct node *r = n->n;
		free(n);
		return r;
	}
	else return n;
};


int main() {
	struct node *head = new_node(-1);
	add(head, 6);
	add(head, 5);
	add(head, 3);
	add(head, 5);
	add(head, 6);
	print_list(head);
	remove_duplicates(head);
	print_list(head);
	return 0;
};
