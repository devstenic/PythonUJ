node = [2,4,32,4,2,5,7,3,2,21]


def remove_head(node):
    if len(node) == 0:
        raise Exception('lista jest pusta!')
    else:
        node.pop(0)

    return node

def remove_tail(node):
    if len(node) == 0:
        raise Exception('lista jest pusta!')
    else:
        node.pop(-1)

    return node

# Zastosowanie.
print(node)
print(remove_head(node))
print(remove_tail(node))
