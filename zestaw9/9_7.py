def count_leafs(top):
    if top == None:
        return 0
    elif(top.left == None and top.right == None):
        return 1
    else:
        return count_leafs(top.left) + count_leafs(top.right)


def count_total(top):
    if top == None:
        return 0
    else:
        l = top.data
        top.data = count_total(top.right) + count_total(top.left)
        return top.data + l
