def pascal_triangle(n):
    """returns a list of lists of integers representing the
    Pascals triangle of n:
    Returns an empty list
    if n <= 0
    You can assume n will be always an integer """
    ret = [[1]]
    if n >= 2:
        ret.append([1, 1])
    for i in range(n - 2):
        tmp = ret[-1]
        add = [1]
        i = 0
        ln = len(tmp) - 1
        while i < ln:
            a = tmp[i]
            b = tmp[i + 1]
            add.append(a + b)
            i += 1
        add.append(1)
        ret.append(add)
    return ret
