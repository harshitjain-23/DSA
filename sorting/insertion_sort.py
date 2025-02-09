def insertion_sort(l):
    for i in range(1,len(l)):
        for j in range(i,0,-1):
            if l[j-1] >= l[j]:
                l[j-1], l[j] = l[j], l[j-1]
    return l

# OR 

def insertion_sort2(l):
    for i in range(1, len(l)):
        j = i
        while j>0 and ( l[j-1] >= l[j]):
            (l[j-1], l[j]) = (l[j], l[j-1])
            j -= 1
    return l



l = [5,9,54,86,12,97,5,1,1,36,94,-2,-1]
print(insertion_sort2(l))
