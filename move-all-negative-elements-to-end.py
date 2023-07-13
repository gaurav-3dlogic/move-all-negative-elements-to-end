def segregateElements(arr, n):
        n = []
        p = []
        
        for i in arr:
            if i >= 0:
                p.append(i)
            else:
                n.append(i)
        c = 0
        for i in p + n:
            arr[c] = i
            c += 1
        return arr
            
arr = [9,-1,9,-6,4,5]
n = len(arr)
        
print(segregateElements(arr, n))