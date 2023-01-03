
#define _CRT_SECURE_NO_WARNINGS
#define TRUE	1
#define FALSE	0

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// stack 사용과 관련된 함수 및 코드 정의
typedef int element;
typedef struct stacknode {
	element data;
	struct stacknode* link;
}stacknode;
stacknode* topnode;

void push(element item) {
	stacknode* temp = (stacknode*)calloc(1, sizeof(stacknode));
	temp->data = item;
	temp->link = topnode;
	topnode = temp;
}

void pop() {
	stacknode* temp = (stacknode*)calloc(1, sizeof(stacknode));
	element item;
	if (topnode == NULL) printf("%d\n", -1);
	else {
		item = topnode->data;
		temp = topnode;
		topnode = topnode->link;
		free(temp);
		printf("%d\n", item);
	}
}

void size() {
	stacknode* temp = (stacknode*)calloc(1, sizeof(stacknode));
	int size = 0;
	temp = topnode;
	while (TRUE) {
		if (temp == NULL) {
			printf("%d\n", size);
			break;
		}
		else {
			temp = temp->link;
			size++;
		}
	}
}

void empty() {
	if (topnode == NULL) printf("%d\n", TRUE);
	else printf("%d\n", FALSE);
}

void top() {
	element item;
	if (topnode == NULL) printf("%d\n", -1);
	else {
		item = topnode->data;
		printf("%d\n", item);
	}
}

void test_10828()
{	
	int num = 0;
	int cnt_i = 0;
	element item = 0;
	char str[10] = { NULL };
	
	scanf("%d", &num);
	char** order = (char**)calloc(num, sizeof(str));
	
	for (cnt_i = 0; cnt_i < num; cnt_i++) {
		scanf("%s", order + cnt_i);
		if (strcmp(order + cnt_i,"push") == 0) scanf("%d", &item);
		if (strcmp(order + cnt_i, "push") == 0) push(item);
		else if (strcmp(order + cnt_i, "pop") == 0) pop();
		else if (strcmp(order + cnt_i, "size") == 0) size();
		else if (strcmp(order + cnt_i, "empty") == 0) empty();
		else if (strcmp(order + cnt_i, "top") == 0) top();
	}
}
int main(){
    test_10828();
    return 0;
}