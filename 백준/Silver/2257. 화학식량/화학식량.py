# 1. 입력 받기
problem = list(input())
# 괄호 안에 공백일 수도 있음

# 2. 화학 식량 계산
stack = []
sub_count = 0
for i in range(len(problem)):
    stack.append(problem[i])

    if stack[-1] == "H":
        stack[-1] = 1
    elif stack[-1] == "C":
        stack[-1] = 12
    elif stack[-1] == "O":
        stack[-1] = 16
    elif "2" <= stack[-1] and stack[-1] <= "9":
        stack[-2] *= int(stack[-1])
        stack.pop()
    elif stack[-1] == ")":
        stack.pop()
        while stack[-1] != "(":
            sub_count += stack[-1]
            stack.pop()
        stack.pop()
        stack.append(sub_count)
        sub_count = 0
    else:
        continue

print(sum(stack))