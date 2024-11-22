array1 = [1,2,3,4,5]
array2 = [4,5,4]

def intersect(array1, array2):
    result = []
    for i in array1:
        for j in array2:
            if i == j and j not in result:
                result.append(j)
    return result

print(intersect(array1, array2))
