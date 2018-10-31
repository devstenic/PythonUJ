L = ['sd', 'dsd', 'dshi', 'sdh', 'hdishd', 'dus', 'sdhgusgu']

def iterOdwracanie(L ,left, right):
    right += 1
    length = len(L[left:right])
    s = length
    nList = [None]*length
    for i in L[left:right]:
        s -= 1
        nList[s] = i
    return nList


print(iterOdwracanie(L, 2, 5))


def rekuOdwracanie(L, left, right):
    L[right], L[left] = L[left], L[right]
    if abs(right-left) != 0:
        rekuOdwracanie(L, left+1, right-1)

print(rekuOdwracanie(L, 2,4))