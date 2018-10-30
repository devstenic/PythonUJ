def sum_seq(seq):
    result = 0
    for i in seq:
        if isinstance(i, (list, tuple)):
            result += sum_seq(i)
        else:
            result += i
    return result


seq = [3,5,6,[4,5,6],7, [6,7]]

print(sum_seq(seq))