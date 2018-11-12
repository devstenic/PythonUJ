L = ['sd', 'dsd', 'dshi', 'sdh', 'hdishd', 'dus', 'sdhgusgu']

def iterOdwracanie(L ,left, right):
    left += len(L) if left < 0 else 0
    right += len(L) if right < 0 else 0
    while left < right:
        L[left], L[right] = L[right], L[left]
        left = left + 1
        right = right - 1
    return L

print(iterOdwracanie(L, 2, 5))


def rekuOdwracanie(L, left, right):
    left += len(L) if left < 0 else 0
    right += len(L) if right < 0 else 0
    if left < right:
        L[left], L[right] = L[right], L[left]
        return L
        rekuOdwracanie(L, left + 1, right - 1)


print(rekuOdwracanie(L, 2,4))