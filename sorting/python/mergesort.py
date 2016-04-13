def merge_sort(arr):
    return _merge_sort(arr,0,len(arr)-1)

def _merge_sort(arr,start,end):
    mid = (end+start)/2
    if start<end:
        _merge_sort(arr,start,mid)
        _merge_sort(arr,mid+1,end)

    current,left,right = 0,start,mid+1
    temp = [None] * (end - start + 1)
    while left<=mid and right<= end:
        if arr[left] <= arr[right]:
            temp[current] = arr[left]
            left = left+1
        else:
            temp[current] = arr[right]
            right = right+1
        current = current+1

    if left<=mid:
        temp[current:] = arr[left:mid+1]
    if right<=end:
        temp[current:] = arr[right:end+1]

    current = 0
    while start<=end:
        arr[start] = temp[current]
        current+=1
        start+=1
    return arr

array = [99,22,66,77,88,100]
print(array)
print(merge_sort(array))
