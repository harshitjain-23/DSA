def bubble(l):

    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l
            

l = [5,9,54,86,12,97,5,1,1,36,94,-2,-1]
print(bubble(l))