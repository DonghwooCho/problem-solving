import sys

# 1. 입력 받기
target = "_"
stack = []
res = True

while True:
    target = sys.stdin.readline().rstrip()
    stack = []
    res = True
    
# 2. 문자열 순회하면서 균형 여부 출력
    if target == ".":
        break

    for element in target:
        if element == "(" or element == "[":
            stack.append(element)
        elif element == ")":
            if not stack or stack[-1] != "(":
                print("no")
                res = False
                break
            else:
                stack.pop()
        elif element == "]":
            if not stack or stack[-1] != "[":
                print("no")
                res = False
                break
            else:
                stack.pop()

    if res:
        if not stack:
            print("yes")
        else:
            print("no")