# 1. 입력 받기
N = int(input())

words = [0] * N
for i in range(N):
    words[i] = input()

# 2. 단어의 합 최댓 값 출력 하기
words.sort(key = lambda x: len(x), reverse = True)
translation = []
for i in range(N):
    words[i] = list(words[i])
    for j in range(len(words[i])):
            translation.append([words[i][j], len(words[i]) - j])

dic_targets = {}
for target in translation:
    if not target[0] in dic_targets:
        dic_targets[target[0]] = pow(10, target[1] - 1)
    else:
        dic_targets[target[0]] += pow(10, target[1] - 1)

res = sorted(dic_targets.values(), reverse = True)

n = 9
sum = 0
for target in res:
    sum += n * target
    n -= 1

print(sum)