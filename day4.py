# #moves zeros to end
# nums = list(map(int, input().split()))
# i = 0 
# for j in range(len(nums)):
#       if nums[j] != 0:
#             nums[i],nums[j] = nums[j],nums[i]
#             i += 1
# print(nums)            

#remove duplicates from sorted array
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