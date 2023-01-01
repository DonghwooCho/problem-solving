# 1. 입력 받기
P, K = map(int, input().split())

# 2. 암호 성능 판단 후 출력
p = -1
q = -1
for i in range(2, K):
    if P % i == 0:
        p = i
        q = P // p
        break

r = min(p, q)
if r == -1:
    print("GOOD")
else:
    print("BAD %d" % (r))