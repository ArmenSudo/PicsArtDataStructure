def ackermann(x, y):
    if y == 0:
        return 0
    elif x == 0:
        return 2 * y
    elif y == 1:
        return 2
    else:
        return ackermann(x - 1, ackermann(x, y - 1))


def a3(n):
    return ackermann(2, n)


print(a3(4))
# 2 * 2 ** (n - 1)
#
# 2 * ackermann(1, ackermann(2, n - 2) -> 2 * 2 * ackermann(1, ackermann(2, n - 3) ->
# 2 * 2 * 2 * ackermann(1, ackermann(2, n - 4)


# 1 -> 2
# 2 -> 4
# 3 -> 16
# 4 -> 65536
# 2**(a3(n-1))
