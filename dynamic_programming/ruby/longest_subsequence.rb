def longest_sub(arr)
  # temp is for saving previous longest subsequence
  temp = [1]*arr.count
  for i in 1...arr.count
    for j in 0..i
      if arr[j] < arr[i]
        if  temp[j] >= temp[i]
         temp[i] = temp[j]+1
        end
      end
    end
  end
  return temp.max
end


# Problem example: http://www.practice.geeksforgeeks.org/problem-page.php?pid=134

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
puts longest_sub(arr)==6
