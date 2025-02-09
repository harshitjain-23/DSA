def binary(l,v,m,n):
    while m <= n:
        mid = (m+n) // 2
        if l[mid] == v:
            return True
        elif l[mid] > v:
            return binary(l,v,m,mid-1)
        elif l[mid] < v: 
            return binary(l,v,mid+1,n)       
        else:
            return False


l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
m = 0
n = len(l) - 1
print(binary(l,-2,m,n))
