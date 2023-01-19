N = int(input())

res = [0] * N
for i in range(N):
    res[i] = int(input())
   
res.sort()
for i in range(N):
    print(res[i])