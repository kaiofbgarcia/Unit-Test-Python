from logging.config import valid_ident

def Max(values):

    max = values[0]

    for i in range(len(values)):
        if max < values[i]:
            max = values[i]
    return max

def Min(values):
    min = values[0]

    for i in range(len(values)):
        if min > values[i]:
            min = values[i]

    return min

def MaxMin(values):

    maxmin = []

    if len(values) == 0:
        return False
    else:
        maxmin.append(Max(values))
        maxmin.append(Min(values))
    
    return maxmin