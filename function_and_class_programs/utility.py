def greatestNumber(list) :
    greatest = list[0]
    for i in list :
        if greatest < i :
            greatest = i
    return greatest

def smallestNumber(list) :
    smallest = list[0]
    for i in list :
        if smallest > i :
            smallest = i
    return smallest
