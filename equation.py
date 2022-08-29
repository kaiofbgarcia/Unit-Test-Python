from math import sqrt

def getRoots(a, b, c):
    roots = []

    if(a == 0):
        return -1
    
    delta = (b * b) - (4 * a * c)

    if delta > 0:
        roots.append((-b + sqrt(delta)) / (2*a))
        roots.append((-b - sqrt(delta)) / (2*a))

    elif delta == 0:
        roots.append(-b / (2*a))

    else:
        roots = []

    return roots