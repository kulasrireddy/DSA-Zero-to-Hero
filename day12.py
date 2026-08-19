#Maximum subarray (Brute force)
nums = list(map(int, input().split()))
max_sum = nums[0]

for i in range(len(nums)):
      curr_sum = 0
      
      for j in range(i, len(nums)):
            curr_sum+=nums[j]
            
            if curr_sum > max_sum:
                  max_sum = curr_sum
print(max_sum)            

#Kadane's alog
nums = list(map(int, input().split()))
max_sum = nums[0]
curr_sum = nums[0]
for i in range(1,len(nums)):
      curr_sum = max(nums[i],curr_sum + nums[i])
      max_sum = max(curr_sum, max_sum)
print(max_sum)    

#Intersection of two arrays
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
seen1 = set(nums1)
seen2 = set(nums2)
res = []
for num in seen1:
      if num in seen2:
            res.append(num)
print(res)              
            