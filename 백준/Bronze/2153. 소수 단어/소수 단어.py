def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


word = list(input())
for i in range(len(word)):
    if ord(word[i]) <= 90:
        word[i] = ord(word[i]) - ord('A') + 27
    else:
        word[i] = ord(word[i]) - ord('a') + 1

if is_prime(sum(word)):
    print("It is a prime word.")
else:
    print("It is not a prime word.")
