# 1. 입력 받고 출력하기(예외 처리)
for i in range(100):
    try:
        print(input())
    except EOFError:
        break