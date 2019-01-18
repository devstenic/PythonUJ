def find_max(node):
    if node is None:
        raise ValueError("Lista jest pusta!")

    maxValue = node
    while node:
        if node.data > maxValue.data:
            maxValue = node
        node = node.next

    return maxValue


def find_min(node):
    if node is None:
        raise ValueError("Pusta lista")

    minValue = node
    while node:
        if node.data < minValue.data:
            minValue = node
        node = node.next

    return minValue
