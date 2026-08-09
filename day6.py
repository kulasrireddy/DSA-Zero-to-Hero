# #Missing number in range(single Number)
nums = list(map(int, input().split()))
n = len(nums)
expected_sum = n * ( n + 1) // 2
count = 0
for num in nums:
      count += num
print(count - expected_sum)       

#two sum(Nested Loop)
nums = list(map(int, input().split()))
target = int(input())
for i in range(0, len(nums)):
      for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                  print(i, j)

#Dictionay which reduces the tc
nums = list(map(int, input().split()))
target = int(input())
seen = {}
for i in range(0,len(nums)):
      diff = target - nums[i]
      if diff in seen:
            print(seen[diff], i)
      seen[nums[i]] = i
            
                  
      
                                   
            