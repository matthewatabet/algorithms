/*
 * Partition a linked list by value.
 */

#include <stdlib.h>
#include <stdio.h>


struct node {
        int value;
        struct node *next;
};


struct list {
        struct node *head;
};


void node_print(struct node *n) {
        if ( NULL == n ) printf("Node: NULL\n");
        else printf("Node: %d\n", n->value);
}


struct node *node_new(int value) {
        struct node *n = malloc(sizeof(*n));
        n->next = NULL;
        n->value = value;
        return n;
}


struct node *node_add(struct node *n, int value) {
        if ( NULL == n ) return node_new(value);
        else {
                n->next = node_add(n->next, value);
                return n;
        }
}


struct list *list_new() {
        struct list *l = malloc(sizeof(*l));
        l->head = NULL;
        return l;
}


void list_free(struct list *l) {
    struct node *n = l->head;
    struct node *current = NULL;
    while ( NULL != n ) {
            current = n;
            n = n->next;
            free(current);
    }
    free(l);
}


void list_print(struct list *l) {
        struct node *n = l->head;
        while (NULL != n) {
                printf("%d ", n->value);
                n = n->next;
        }
        printf("\n");
}


void list_add(struct list *l, int value) {
        l->head = node_add(l->head, value);
}


struct node *npartition(struct node *n, int pivot, struct node **tail) {
        if ( NULL == n->next ) {
                *tail = n;
                return n;
        }

        struct node *next = npartition(n->next, pivot, tail);
        if ( next->value > pivot ) {
                n->next = next->next;
                (*tail)->next = next;
                next->next = NULL;
                *tail = next;
        } else n->next = next;

        return n;
}


void partition(struct list* l, int pivot) {
        struct node **tail = malloc(sizeof(*tail));
        l->head = npartition(l->head, pivot, tail);
        free(tail);
}


int main() {
        struct list *l = list_new();
        list_add(l, 3);
        list_add(l, 5);
        list_add(l, 2);
        list_add(l, 6);
        list_add(l, 7);
        list_add(l, 2);
        list_add(l, 4);
        list_print(l);
        partition(l, 4);
        list_print(l);
        list_free(l);
        return 0;
}
