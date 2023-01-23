N = int(input())

count = 0
for i in range(N):
    word = list(input() + '!')
    count += 1
    alpha = []
    for j in range(len(word) - 1):
        if word[j] in alpha:
            count -= 1
            break
        if word[j] != word[j+1]:
            alpha.append(word[j])

print(count)
