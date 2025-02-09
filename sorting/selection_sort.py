def selection(l):
    for i in range(len(l)):
        min = i 
        for j in range(i+1,len(l)):
            if l[j] < l[min]:
                min = j 
        l[i], l[min] = l[min], l[i]
    return l 
 

l = [5,9,54,86,12,97,5,1,1,36,94,-2,-1]
print(selection(l))