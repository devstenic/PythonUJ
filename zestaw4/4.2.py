def miarka(length):
    lineUp = '|'
    lineDown = '0'
    for i in range(length):
        lineUp += '....|'
        if i < 10:
            lineDown += '    {0}'.format(i + 1)
        else:
            lineDown += '   {0}'.format(i + 1)
    result = lineUp + '\n' + lineDown
    return result

print(miarka(7))

def prostokat(width, height):
    pWidth = "+"
    kWidth = "---+"
    pHeight = "|"
    kHeight = "   |"

    A = pWidth + width * kWidth + ""
    B = pHeight + width * kHeight + ""

    result = ""

    for x in range(height):
        result = result + A + "\n"
        result = result + B + "\n"

    result = result + A + "\n"
    return result
print(prostokat(3,5))