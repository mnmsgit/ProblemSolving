// py로 다시 풀기
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int total,left,output = 0;
	scanf("%d", &total);
	left = total % 5;
	if (left == 0) {
		output = total / 5;
	}
	else if (left == 1) {
		if (total < 6)
		{
			output = -1;
		}
		else
		{
			output = (total - 6) / 5 + 2;
		}
	}
	else if (left == 2) {
		if (total < 12) {
			output = -1;
		}
		else {
			output = (total - 12) / 5 + 4;
		}
	}
	else if (left == 3) {
		if (total < 3) {
			output = -1;
		}
		else{
			output = (total - 3) / 5 + 1;
		}
	}
	else {
		if (total < 9) {
			output = -1;
		}
		else {
			output = (total - 9) / 5 + 3;
		}
	}
	
	printf("%d", output);
	return 0;
	}
	
