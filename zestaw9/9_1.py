node = [2,4,32,4,2,5,7]


def remove_head(node):
    if node.len() == 0:
        raise Exception('lista jest pusta!')
    else:
        node.pop(0)

    return node

def remove_tail(node):
    if node.len() == 0:
        raise Exception('lista jest pusta!')
    else:
        node.pop(-1)

    return node

# Zastosowanie.
print(node)