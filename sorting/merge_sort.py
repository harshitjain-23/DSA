def merge(l,m):
    x,y = len(l), len(m)
    (c,i,j) = ([],0,0)

    while i < x and j < y:
        if l[i] <= m[j]:
            c.append(l[i])
            i += 1
        else:
            c.append(m[j])
            j += 1

    
    while i < x:
        c.append(l[i])
        i += 1

    while j < y:
        c.append(m[j])
        j += 1

    return (c)
    

def merge_sort(l):
    n = len(l) 

    if n <= 1:
        return (l)
    
    left = merge_sort(l[:n// 2])
    right = merge_sort(l[n// 2:])
    sorted_list = merge(left,right)

    return (sorted_list)

l = [15,10,5,20,25,30,40,35]
# l = [5,9,54,86,12,97,5,1,1,36,94,-2,-1]
print(merge_sort(l))





