# #Reverse an array
# nums = list(map(int, input().split()))
# i = 0
# j = len(nums) - 1
# while i < j:
#       nums[i],nums[j] = nums[j],nums[i]
#       i += 1
#       j -= 1
# print(nums)

#Count frequency of target in array
nums = list(map(int, input().split()))
target = int(input())
count = 0
for num in range(len(nums)):
      if nums[num]==target:
            count += 1
print(count)    
            