/*
 * Check if one string is a permutation of the other.
 * Use a counter array to keep track of how often characters appear in
 * each string. Assumes ascii characters.
 *
 * Check length of strings.
 * Initialize two counter arrays.
 * Count characters in each string via count().
 * Compare the array values.
 *     Early return if disimilar.
 */
#include <string.h>
#include <stdlib.h>
#include <stdio.h>


void count(char *str, int *counter, int n)
{
	int c;
	int i;
	for ( i = 0; i < n; i++)
	{
		c = (int) str[i];
		counter[c] += 1;
	}
}


int perm(char *a, char *b)
{
	size_t a_len = strlen(a);
	size_t b_len = strlen(b);

	if ( a_len != b_len ) return 0;
	
	int a_count[128] = {};
	int b_count[128] = {}; 
	
	count(a, a_count, a_len);
	count(b, b_count, b_len);

	// compare the results.
	int i;
	for ( i = 0; i < 128; i++)
	{
		if ( a_count[i] != b_count[i] )
		{
			return 0;
		}
	}

	return 1;
}


int main()
{
	printf("%d\n", perm("this", "siht"));
	printf("%d\n", perm("abc", "cba"));
	printf("%d\n", perm("fool", "foo"));
	printf("%d\n", perm("yop", "fop"));
	printf("%d\n", perm("this way", "way this"));
}
