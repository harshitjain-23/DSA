def quick_sort(l):
    if len(l) <= 1:
        return l
    
    pivot = l[-1]
    A, B = [],[]

    for i in range(len(l)-1):
        if l[i] <= pivot:
            A.append(l[i])
        else:
            B.append(l[i])

    return (quick_sort(A) + [pivot] + quick_sort(B))


l = [5,9,54,86,12,97,5,1,1,36,94,-2,-1]
print(quick_sort(l))