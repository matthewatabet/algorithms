/*
 * Test if a linked list is a palindrome.
 */

#include <stdlib.h>
#include <stdio.h>


struct node {
        int value;
        struct node* next;
};


struct list {
        struct node* head;
        struct node* tail;
};


struct node* node_new(int value) {
        struct node *n = malloc(sizeof(*n));
        n->value = value;
        n->next = NULL;
        return n;
}


struct list* list_new() {
        struct list *l = malloc(sizeof(*l));
        l->head = NULL;
        l->tail = NULL;
        return l;
}


void list_add(struct list *l, int value) {
        struct node *n = node_new(value);
        if ( NULL == l->tail && NULL == l->head ) {
                l->head = n;
                l->tail = n;
        }
        else {
            l->tail -> next = n;
            l->tail = n;
        }
}


void list_print(struct list *l) {
        struct node *n = l->head;
        while ( NULL != n ) {
                printf("%d ", n->value);
                n = n->next;
        }
}


void list_reverse_n(struct list *l, struct node *n) {
        if ( NULL == n ) return;
        list_reverse_n(l, n->next);
        list_add(l, n->value);
}


struct list *list_reverse(struct list *l) {
        struct list *r = list_new();
        list_reverse_n(r, l->head);
        return r;
}


int list_comp(struct list *a, struct list *b) {
        struct node *x = a->head;
        struct node *y = b->head;
        while ( NULL != x && NULL != y ) {
                if ( x -> value != y -> value ) return 0;
                x = x->next;
                y = y->next;
        }

        if ( NULL == x && NULL == y ) return 1;
        else return 0;
}


int list_palindrome(struct list *n) {
        struct list *r = list_reverse(n);
        return list_comp(n, r);
}


int main() {
        struct list *a = list_new();
        list_add(a, 5);
        list_add(a, 4);
        list_add(a, 2);
        list_add(a, 4);
        list_add(a, 5);
        printf("%d\n", list_palindrome(a));

        struct list *b = list_new();
        list_add(b, 2);
        list_add(b, 3);
        list_add(b, 3);
        list_add(b, 1);
        printf("%d\n", list_palindrome(b));

        return 0;
}
