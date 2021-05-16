import sys
def wrong(arr):
    return "Wrong sorting method"

def swap(i, j):
    return j, i

def bubblesort(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = swap(arr[j], arr[j+1])
    return arr
    
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    tmp1 = []
    tmp2 = []
    # if (r-l) <= 1:
    #     return arr
    for i in range(n1):
        tmp1.append(arr[l+i])
    for i in range(n2):
        tmp2.append(arr[m+1+i])
    i = 0
    j = 0
    k = l
    while(i < n1 and j < n2):
        if tmp1[i] <= tmp2[j]:
            arr[k] = tmp1[i]
            i+=1
        else:
            arr[k] = tmp2[j]
            j+=1
        k+=1
    while(i<n1):
        arr[k] = tmp1[i]
        i+=1
        k+=1
    while(j<n2):
        arr[k] = tmp2[j]
        j+=1
        k+=1
    return arr

def mergesort(arr, l, r):
    if l<r:
        mid = l + (r-l)//2
        arr = mergesort(arr, l, mid)
        arr = mergesort(arr, mid+1, r)
        arr = merge(arr, l, mid, r)
    return arr

def mergesortinit(arr):
    n = len(arr)
    return mergesort(arr, 0, n-1)
def insertionsort(arr):
    n = len(arr)
    for i in range(1,n):
        point = -1
        for j in range(0,i):
            if arr[i] < arr[j]:
                point = j
                break
        if point != -1:
            tmp = arr[i]
            for j in range(i, point, -1):
                arr[j] = arr[j-1]
            arr[point] = tmp
    return arr
   
def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        minelem = arr[i]
        minloc = i
        for j in range(i, n):
            if arr[j] < minelem:
                minelem = arr[j]
                minloc = j
        arr[minloc], arr[i] = swap(arr[minloc], arr[i])
    return arr
    
def defaultsort(arr): # Sort using python default Timsort
    arr.sort()
    return arr
    
def stringlongsort(arr): # Sorting using the key of sort
    arr.sort(lambda x: len(x))
    return arr
    
sorts = {
    'bubble': bubblesort,
    'insert': insertionsort,
    'select': selectionsort,
    'merge': mergesortinit,
    'default': defaultsort,
    'stringlong': stringlongsort
}


print("Enter the array:")
arr = list(map(int, input().split(' ')))
print(sorts.get(sys.argv[1], wrong)(arr)) if len(sys.argv) > 1 else print(wrong(arr))