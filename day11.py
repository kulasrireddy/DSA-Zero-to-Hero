# #contain duplicates using dict
# nums = list(map(int, input().split()))
# freq = {}
# for num in nums:
#       if num in freq:
#             freq[num] += 1
#       else:
#             freq[num] = 1
# for val in freq.values():
#       if val > 1:
#             print("True")
#             break
# else:
#       print("False")       

#contains duplicates using set()
# nums = list(map(int, input().split()))
# seen = set()
# for num in nums:
#       if num in seen:
#             print("True")
#             break
#       seen.add(num)  
# else:
#       print("False") 

#range sum query(brute force)
# nums = list(map(int, input().split()))
# left = int(input())
# right = int(input())
# count = 0
# for num in range(left , right + 1):
#       count += nums[num]
# print(count)      
      
#range sum query
nums = list(map(int, input().split()))
left = int(input())
right = int(input())
prefix_sum = []
new_sum = 0
for num in nums:
      new_sum += num
      prefix_sum.append(new_sum)
if left == 0:
      ans = prefix_sum[right]
else:
      ans = prefix_sum[right] - prefix_sum[left - 1]
print(ans)