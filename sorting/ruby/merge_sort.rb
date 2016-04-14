## Note: Ruby arrays are pass by reference instead of pass by value.

def merge_sort(arr)
  return merge_sort_f(arr,0,arr.count-1)
end

def merge_sort_f(arr,start,fin)
  mid = (start+fin)/2
  if start<fin
    merge_sort_f(arr,start,mid)
    merge_sort_f(arr,mid+1,fin)
  end
  current=0
  left = start
  right = mid +1
  temp = [nil]*(fin-start+1)
  while (left<=mid and right <=fin)
    if arr[left] <= arr[right]
      temp[current] = arr[left]
      left = left+1
    else
      temp[current] = arr[right]
      right = right+1
    end
    current = current+1
  end
  if left<=mid
    temp[current,(fin-start+1)] = arr[left,mid+1]
  end
  if right<=fin
    temp[current,(fin-start+1)] = arr[right,fin+1]
  end
  current = 0
  while start<=fin
    arr[start] = temp[current]
    current+=1
    start+=1
  end
  return arr
end
arr = [5,10,2,4,6]
print arr
puts ""
merge_sort(arr)
print arr
