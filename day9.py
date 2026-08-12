# #maximum consecutive one's
nums = list(map(int, input().split()))
count = 0
max_count = 0
for num in nums:
      if num == 1:
            count += 1
            if count > max_count:
                  max_count = count
      else:
            count = 0
print(max_count)                 

#Single Number
nums = list(map(int, input().split()))
freq = {}
for num in nums:
      if num in freq:
            freq[num] += 1
      else:
            freq[num] = 1
for i, j in freq.items():
      if j == 1:
            print(i)   
                                                                                                       
#Single number by (XOR method)
nums = list(map(int, input().split()))
res = 0
for num in nums:
      res ^= num
print(res)      