
def swap(x, y, values):
    values[y], values[x] = values[x], values[y]

def bubblesort(values):

    swaped = False

    len_arr = len(values) - 1

    for i in range(len_arr):

        for j in range(len_arr - i):
            if values[j] > values[j + 1]:
                swaped = True
                swap(j + 1, j, values)
        
        if not swaped:
            return values
    
    return values