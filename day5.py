#Remove elements
# nums = list(map(int, input().split()))
# val = int(input())
# i = 0
# j = 0
# while j < len(nums):
#       if nums[j] != val:
#             nums[i] = nums[j]
#             i += 1
#       j += 1
# print(i)   

#Merge two sorted arrays
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))         
res = []
i = 0
j = 0
while i < len(nums1) and j < len(nums2):
      if nums1[i] < nums2[j]:
            res.append(nums1[i])
            i += 1
            
      elif nums2[j] < nums1[i]:
            res.append(nums2[j])
            j += 1
      else:
            res.append(nums1[i])
            res.append(nums2[j])
            i += 1
            j += 1
while i < len(nums1):
      res.append(nums1[i])
      i += 1
while j < len(nums2):
      res.append(nums2[j])
      j += 1
print(res)
         