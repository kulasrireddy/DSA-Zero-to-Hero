#Day 7 is revision of the 6 days
#1.Move zeros to end
nums = list(map(int, input().split()))
i = 0
for j in range(0,len(nums)):
      if nums[j] != 0:
            nums[j],nums[i] = nums[i],nums[j]
            i += 1
print(nums)             

#2.Remove duplicates from sorted array
nums = list(map(int, input().split()))
i = 0
j = 1
while j < len(nums):
      if nums[i] == nums[j]:
            j += 1
      else:
            i += 1
            nums[i] = nums[j]
            j += 1
print(nums[:i+1])     

#3.Second largest number in an array
nums = list(map(int, input().split()))
largest = second_largest = float('-inf')
for num in nums:
      if num > largest:
            second_largest = largest
            largest = num 
      elif num > second_largest and num != largest:
            second_largest = num
if second_largest == float('-inf'):
      print(-1)
else:
      print(second_largest)  

#4.Missing number in a range
nums = list(map(int, input().split()))
n = len(nums)
expected = n * (n + 1) // 2
actual = 0
for num in nums:
      actual += num
print(expected - actual)  

#5.Check array is sorted
nums = list(map(int, input().split()))
for num in range(len(nums) - 1):
      if nums[num] > nums[num+1]:
            print("False")
            break
else:
      print("True")         

#6.Reverse an array
nums = list(map(int, input().split()))
i = 0
j = len(nums) - 1
while i < j:
      nums[i],nums[j] = nums[j],nums[i]
      i += 1
      j -= 1
print(nums)

#7.Remove element in an array(in-place)
nums = list(map(int, input().split()))
value = int(input())
i = 0
for j in range(0,len(nums)):
      if nums[j] != value:
            nums[i] = nums[j]
            i += 1
print(i)    

#8.Merge two sorted arrays
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
res = []
i = 0
j = 0
while i < len(nums1) and j < len(nums2):
      if nums1[i] <= nums2[j]:
            res.append(nums1[i])
            i += 1
      elif nums2[j] <= nums1[i]:
            res.append(nums2[j]) 
            j += 1
while i < len(nums1):
      res.append(nums1[i])
      i += 1
while j < len(nums2):
      res.append(nums2[j])
      j += 1
print(res)                                    

#9.Linear Search
nums = list(map(int, input().split()))
target = int(input())
for i in range(len(nums)):
      if nums[i] == target:
            print(i)
            break
else:
      print(-1)     

#10.Count Frequency of target
nums = list(map(int, input().split()))
target = int(input())
count = 0
for i in nums:
      if i == target: 
            count += 1
print(count)          

#11.Largest number
nums = list(map(int, input().split()))
largest = float('-inf')
for num in nums:
      if num > largest:
            largest = num
print(largest)

#12.Two Sum
nums = list(map(int, input().split()))
target = int(input())
seen = {}
for i in range(len(nums)):
      diff = target - nums[i]
      if diff in seen:
            print(seen[diff],i)
            break
      seen[nums[i]] = i 
            
