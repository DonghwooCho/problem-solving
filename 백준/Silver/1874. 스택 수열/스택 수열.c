
#define _CRT_SECURE_NO_WARNINGS
#define TRUE	1
#define FALSE	0

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// stack 사용과 관련된 함수 및 코드 정의
// 연결리스트 stack 노드 정의
typedef int element;
typedef struct stacknode {
	element data;
	struct stacknode* link;
}stacknode;
stacknode* topnode;

// test10828 함수
void push(element item) {
	stacknode* temp = (stacknode*)calloc(1, sizeof(stacknode));
	temp->data = item;
	temp->link = topnode;
	topnode = temp;
}

element pop() {
	stacknode* temp = (stacknode*)calloc(1, sizeof(stacknode));
	element item;
	if (topnode == NULL) return -1;
	else {
		item = topnode->data;
		temp = topnode;
		topnode = topnode->link;
		free(temp);
		return item;
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

element top() {
	element item;
	if (topnode == NULL) return -1;
	else {
		item = topnode->data;
		return item;
	}
}

void test_10828()
{	
	topnode = NULL;
	int num = 0;
	int cnt_i = 0;
	char str[10] = { NULL };
	element item = 0;

	
	scanf("%d", &num);
	char** order = (char**)calloc(num, sizeof(str));

	for (cnt_i = 0; cnt_i < num; cnt_i++) {
		scanf("%s", order + cnt_i);
		if (strcmp(order + cnt_i, "push") == 0){
			scanf("%d", &item);
			push(item);
		}
		else if (strcmp(order + cnt_i, "pop") == 0) printf("%d\n", pop());
		else if (strcmp(order + cnt_i, "size") == 0) size();
		else if (strcmp(order + cnt_i, "empty") == 0) empty();
		else if (strcmp(order + cnt_i, "top") == 0) printf("%d\n", top());

	}
}

void test_1874()
{
	topnode = NULL;
	element item = 0;
	element temp = 0;
	int cnt_i = 0;
	int max = 0;
	int num = 0;
	scanf("%d", &num);
	int* sequence = (int*)calloc(num, sizeof(int));
	push(item);
	for (cnt_i = 0; cnt_i < num; cnt_i++){
		scanf("%d", &sequence[cnt_i]);
		if (sequence[cnt_i] == num) max = cnt_i;
	}
	for (cnt_i = max; cnt_i < num; cnt_i++) {
		if (sequence[cnt_i] < sequence[cnt_i + 1]) {
			printf("NO\n");
			return;
		}
	}//31542
	for (cnt_i = 0; cnt_i < num; cnt_i++) {
		while (sequence[cnt_i] > topnode->data) {
			item++;
			push(item);
		}
		if (sequence[cnt_i] == topnode->data) {
			temp = pop();
		}
		else {
			printf("NO\n");
			return;
		}
	

	}
	item = 0;
	for (cnt_i = 0; cnt_i < num; cnt_i++) {
		while (sequence[cnt_i] > topnode->data) {
			item++;
			push(item);
			printf("+\n");
		}
		if (sequence[cnt_i] == topnode->data) {
			temp = pop();
			printf("-\n");
		}
		else {
			printf("NO\n");
			return;
		}
	}
}

void test_17298(){

}

int main()
{
	//test_10828();
	test_1874();
	//test_17298();

	getchar();
	return 0;
}

// EOF

