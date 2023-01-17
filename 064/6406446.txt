// ITP1_7_C:   Spreadsheet
// 2017.7.27

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int main()
{
	int e[101][101];
	int R, C, r, c;
	int s, total;

	scanf("%d%d", &R, &C);
	for (r = 1; r <= R; r++) {
		for (c= 1; c <= C; c++) scanf("%d", &e[r][c]);
	}
	
	for (r = 1; r <= R; r++) {
		s = 0;
		for (c = 1; c <= C; c++) s += e[r][c];
		e[r][0] = s;
	}
	total = 0;
	for (c = 1; c <= C; c++) {
		s = 0;
		for (r = 1; r <= R; r++) s += e[r][c];
		e[0][c] = s;
		total += s;
	}
	for (r = 1; r <= R; r++) {
		for (c = 1; c <= C; c++) printf("%d ", e[r][c]);
		printf("%d\n", e[r][0]);
	}
	for (c = 1; c <= C; c++) printf("%d ", e[0][c]);
	printf("%d\n", total);
	return 0;
}
