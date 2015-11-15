/*
 * Return 1 if the string is a permutation of a palindrome.
 * Sort the string, then count the number of contiguous characters.
 * Only one odd count may be found.
 */

#include <stdlib.h>
#include <string.h>
#include <stdio.h>


void swap(char *s, int i, int j)
{
	char t = s[i];
	s[i] = s[j];
	s[j] = t;
}


int partition(char *s, int lo, int hi)
{
	int i = lo;
	int j = hi + 1;
	char v = s[lo];

	while ( i < j )
	{
		// scan right.
		while ( ++i <= j && i < hi && s[i] <= v );

		// scan left.
		while ( --j >= i && j > lo && s[j] > v );

		// are we done?
		if ( i >= j ) break;

		swap(s, i, j);
	}

	swap(s, lo, j);
	return j;
}


void quicksortr(char *s, int lo, int hi)
{
	if ( lo >= hi ) return;
	int j = partition(s, lo, hi);	
	quicksortr(s, lo, j-1);
	quicksortr(s, j+1, hi);
}


void quicksort(char *s)
{
	quicksortr(s, 0, strlen(s)-1);
}


int pperm(char *s)
{
	// copy and sort incoming string.
	size_t n = strlen(s);
	char *ss = malloc(sizeof(*ss) * n);
	strcpy(ss, s);
	quicksort(ss);

	// count the number of odd characters.
	char c = NULL;
	int odd = 0;
	int count;

	int i;
	for ( i = 0; i < n; i ++ )
	{
		// character group change.
		if ( ss[i] != c )
		{
			if ( count % 2 == 1 )
			{
				odd ++;
				if (odd > 1 ) break;
			}
			count = 1;
		}
		else count ++;
		c = ss[i];
	}

	free(ss);

	if (odd < 2) return 1;
	else return 0;
}


int main()
{
	printf("%d\n", pperm("abcba"));
	printf("%d\n", pperm("aabbc"));
	printf("%d\n", pperm("fgfg"));
	printf("%d\n", pperm("fgxfg"));
	printf("%d\n", pperm("yypq"));
}
