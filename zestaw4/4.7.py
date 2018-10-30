def flatten(seq):
    if isinstance(seq, (list, tuple)):
        result = []
        if seq:
            result += flatten(seq[0])
            result += flatten(seq[1:])
        return result
    else:
        return [seq]


seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]

print(flatten(seq))