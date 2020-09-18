def quicksort(List):

    if len(List)<2:
        return List

    standard=List[0]

    Left=[]
    Right=[]
    for i in range(1,len(List)):
        if List[i]<standard:
            Left.append(List[i])
        else:
            Right.append(List[i])
    
    return quicksort(Left)+[standard]+quicksort(Right)

print(quicksort([[1,4],[0,4]]))

            