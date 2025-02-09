def binary(l,m):
    
    if l == []:
        return False
    
    n = len(l) // 2

    if l[n] == m:
        return True
        
    elif l[n] > m:
        return binary(l[:n],m)

    else:
        return binary(l[n+1:],m)
    


l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(binary(l,5))