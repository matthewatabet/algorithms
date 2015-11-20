/*
 * Given two integers stored as linked lists, sum them together and return
 * another linked list of the sum.
 */

#include <stdlib.h>
#include <stdio.h>


struct list {
        struct node* head;
        struct node* tail;
};


struct node {
        int value;
        struct node *next;
};

struct node *node_new(int v) {
        struct node *n = malloc(sizeof(*n));
        n->value = v;
        n->next = NULL;
        return n;
}


struct list *list_new() {
        struct list *l = malloc(sizeof(*l));
        l->head = NULL;
        l->tail = NULL;
        return l;
}


void list_prepend(struct list *l, int v) {
        struct node *n = node_new(v);
        if ( NULL == l->head && NULL == l->tail ) {
                l->head = n;
                l->tail = n;
        } else {
                n->next = l->head;
                l->head = n;
        }
}


void list_add(struct list *l, int v) {
        struct node *n = node_new(v);
        if ( NULL == l->head && NULL == l->tail ) {
                l->head = n;
                l->tail = n;
        } else {
                l->tail->next = n;
                l->tail = n;
        }
}


void list_print(struct list *l) {
        struct node *n = l->head;
        while (NULL != n) {
                printf("%d ", n->value);
                n = n->next;
        }
        printf("\n");
}


int list_sum(struct list *l) {
        int sum = 0;
        struct node *n = l->head;
        while ( NULL != n ) {
                sum *= 10;
                sum += n->value;
                n = n->next;
        }
        return sum;
}


struct list *int_to_list(int a) {
        struct list *l = list_new();
        while ( a != 0 ) {
                list_prepend(l, a % 10);
                a /= 10;
        }
        return l;
}


struct list *add_lists(struct list *a, struct list *b) {
        int sum_a = list_sum(a);
        int sum_b = list_sum(b);
        int sum_c = sum_a + sum_b;
        return int_to_list(sum_c);
}


int main() {
        struct list *a = int_to_list(321);
        struct list *b = int_to_list(45);
        list_print(a);
        list_print(b);
        list_print(add_lists(a, b));
        return 0;
}
