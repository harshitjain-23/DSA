def search(l,n):
    for i in range(len(l)):
        if l[i] == n:
            return True
    else:
        return False

l = [2,82,24,63,29,8] 
print(search(l,24))   
    