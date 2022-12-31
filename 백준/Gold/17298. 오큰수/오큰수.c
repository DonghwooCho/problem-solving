#define _CRT_SECURE_NO_WARNINGS


#include <stdio.h>

#include <stdlib.h>

#include <string.h>


typedef int element;

int numOfElement = 0;


typedef struct stackNode {

    element data;

    struct stackNode* link;

}stackNode;


stackNode* top;


void init()

{

    top = NULL;

}


int isEmpty()

{

    if (top == NULL) {

        return 1;

    }

    else {

        return 0;

    }


}


void push(element item)

{

    stackNode* temp = (stackNode*)calloc(1, sizeof(stackNode));

    temp->data = item;

    temp->link = top;

    top = temp;

    numOfElement += 1;

}


element pop(element* ret)

{

    element item;

    stackNode* temp = top;


    if (top == NULL) {

        //printf("\n\n Stack is empty!\n");

        *ret = -1;

        return 0;

    }

    else {

        item = temp->data;

        top = temp->link;

        free(temp);


        numOfElement -= 1;

        *ret = item;


        return 1;

    }

}


element peek(element* ret)

{

    if (top == NULL) {

        //printf("\n\n Stack is empty!\n");

        return 0;

    }

    else {

        *ret = (top->data);

        return 1;

    }

}

void test17298() {
    int num;
    int data = 0;
    int test = 0;
    int* numbers = NULL;
    int* msg = NULL;
    int cnt = 0;
    int cnt_i;

    scanf("%d", &num);
    numbers = (int*)calloc(num, sizeof(int));
    msg = (int*)calloc(num, sizeof(int));

    for (cnt_i = 0; cnt_i < num; cnt_i++) scanf("%d", &numbers[cnt_i]);
    
    init(); // 스택 초기화
    cnt_i -= 1;
    for (; cnt_i >= 0; cnt_i--) {
        data = numbers[cnt_i];
        while (isEmpty() == 0) {
            peek(&test);
            if (test <= data) pop(&test);
            else break;
        }
        if (isEmpty() == 1) msg[cnt++] = -1;
        else peek(&msg[cnt++]);
        push(numbers[cnt_i]);
    }
    for (cnt_i = cnt - 1; cnt_i >= 0; cnt_i--) printf("%d ", msg[cnt_i]);
}

int main() {
    //test17298_interation();
    test17298();


    getchar();
    return 0;
}
