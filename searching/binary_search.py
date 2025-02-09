def binarysearch(l,n):
    l = sorted(l)
    low = 0
    high = len(l) -1

    while low < high:
        mid = (low + high) // 2

        if n == l[mid]:
            return True
        else:
            if n < l[mid]:
                high = mid-1
            else: 
                low = mid+1
    return False


l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(binarysearch(l,80))