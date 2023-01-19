S = list(input())

S = list(reversed(S))
res = 0
for i in range(len(S)):
    if S[i] in 'ABCDEF':
        temp = ord(S[i]) - ord('A') + 10
    else:
        temp = int(S[i])
    res += pow(16, i) * temp

print(res)