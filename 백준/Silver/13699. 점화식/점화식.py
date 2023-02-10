# Define solution
def solution(n):
    t = [1]
    for i in range(1, n + 1):
        element = 0
        for j in range(len(t)):
            element += t[j] * t[i - j - 1]
        t.append(element)

    return t[-1]


print(solution(int(input())))
