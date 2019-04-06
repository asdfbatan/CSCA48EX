def rsum(L):
    if L == []:
        result = L[0]
    elif isinstance(L[0], list):
        result = rsum(L[0]) + rsum(L[1:])
    else:
        result = L[0] + rsum(L[1:])
    return result


def rmax(L):
    if L == []:
        result = L[0]
    elif isinstance(L[0], list):
        result = rmax(L[0] + L[1:])
    elif L[1] > L[0]:
        result = rmax(L[:1] + L[2:])
    return result


def second_smallest(L):
    if L == []:
        result = L[0]
    elif isinstance(L[0], list):
        result = second_smallest(L[0] + L[1:])
    elif len(L) == 2:
        if L[0] > L[1]:
            result = L[0]
        else:
            result = L[1]
    else:
        if L[0] > L[1] and L[0] >= L[2]:
            result = second_smallest(L[1:])
        elif L[1] > L[0] and L[1] >= L[2]:
            result = second_smallest(L[:1] + L[2:])
        else:
            result = second_smallest(L[:2] + L[3:])
    return result


def sum_max_min(L):
    if L == []:
        result = L[0]
    elif isinstance(L[0], list):
        result = second_smallest(L[0] + L[1:])
    elif len(L) == 1:
        result = 2 * L[0]
    elif len(L) == 2:
        result = L[0] + L[1]
    elif (L[0] - L[1]) * (L[0] - L[2]) <= 0:
        result = sum_max_min(L[1:])
    elif (L[1] - L[0]) * (L[1] - L[2]) <= 0:
        result = sum_max_min(L[:1] + L[2:])
    else:
        result = sum_max_min(L[:2] + L[3:])
    return result
