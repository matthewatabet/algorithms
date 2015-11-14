/*
 * Determine if a string contains duplicate characters.
 * First, perform a quick sort on the string. Then, see
 * if the string contains any repeated characters.
 */
#include <stdlib.h>
#include <string.h>
#include <stdio.h>


void swap(char *str, int i, int j)
{
	char temp = str[i];
	str[i] = str[j];
	str[j] = temp;
}


int partition(char *str, int lo, int hi)
{
	int i = lo;
	int j = hi + 1;
	char p = str[lo];

	while ( i < j )
	{
		// scan right
		while ( ++i < hi && i <= j && str[i] <= p );

		// scan left
		while ( --j > lo && j >= i && str[j] > p);

		if ( i >= j ) break;
		
		swap(str, i, j);
	}
	swap(str, lo, j);
	return j;
}


void quick_sort_range(char *str, int lo, int hi)
{
	if ( lo >= hi ) return;
	int j = partition(str, lo, hi);
	quick_sort_range(str, lo, j - 1);
	quick_sort_range(str, j + 1, hi);
}


void quick_sort(char *str)
{
	quick_sort_range(str, 0, strlen(str) - 1);
}


int duplicates(char *str)
{
	size_t s = strlen(str);
	if ( s == 1 ) return 0;

	char * sorted_str = malloc(sizeof(*sorted_str) * s);
	strcpy(sorted_str, str);
	quick_sort(sorted_str);

	int i = 0;
	int j; 
	for ( j = 1; j < s; j++)
	{
		if ( sorted_str[i] == sorted_str[j] ) {
			free(sorted_str);
			return 1;
		}
		i ++;
	}
	free(sorted_str);
	return 0;
}


int main()
{
	printf("%d\n", duplicates("xyz"));
	printf("%d\n", duplicates("no dupes"));
	printf("%d\n", duplicates("oop"));
	printf("%d\n", duplicates("this has duplicates"));
	printf("%d\n", duplicates("zcvbzy"));
	printf("%d\n", duplicates("zvyada"));
}
