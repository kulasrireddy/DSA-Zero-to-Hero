#Running sum
# nums = list(map(int, input().split()))
# arr = []
# new_sum = 0
# for i in nums:
#       new_sum += i
#       arr.append(new_sum)
# print(arr)      

#Find the pivot index
nums = list(map(int, input().split()))
total = 0
for num in nums:
      total += num
left_sum = 0
for i in range(0, len(nums)):
      right_sum = total - left_sum - nums[i]
      if left_sum == right_sum:
            print(i)
            break
      left_sum += nums[i]         
else:
      print(-1)  