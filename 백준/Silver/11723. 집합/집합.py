import sys

# 1. 입력 받기
M = int(sys.stdin.readline())

# 2. 입력 받은 명령어 처리
result_set = set()
command = []

for i in range(M):
    command = sys.stdin.readline().rstrip()

    if 'add' in command:
        num = int(command.split(' ')[1])
        result_set.add(num)
    elif 'remove' in command:
        num = int(command.split(' ')[1])
        if num in result_set:
            result_set.remove(num) 
        else:
            continue
    elif 'check' in command:
        num = int(command.split(' ')[1])
        if num in result_set:
            print(1)
        else:
            print(0)
    elif 'toggle' in command:
        num = int(command.split(' ')[1])
        if num in result_set:
            result_set.remove(num)
        else:
            result_set.add(num)
    elif 'all' in command:
        result_set = {i + 1 for i in range(20)}
    else:
        result_set = set()