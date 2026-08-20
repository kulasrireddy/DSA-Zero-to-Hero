#Maximum Sum Subarray of Size K
#(Brute Force)
nums = list(map(int, input().split()))
k = int(input())
max_sum = float('-inf')
for i in range(len(nums) -k + 1):
      curr_sum = 0
      for j in range(i, i + k):
            curr_sum += nums[j]
      if curr_sum > max_sum:
            max_sum = curr_sum
print(max_sum)   

#Optimal solution(sliding window)
nums = list(map(int, input().split()))
k = int(input())
first_window_sum = 0
for i in range(k):   
      first_window_sum += nums[i]

max_sum = first_window_sum
for i in range(k, len(nums)):
      first_window_sum = first_window_sum - nums[i-k] + nums[i]
      
      if first_window_sum > max_sum:
            max_sum = first_window_sum
print(max_sum)      

#Maximum Average Subarray of Size K(Sliding window techinque)
nums = list(map(int, input().split()))
k = int(input())
window_sum = 0
for i in range(k):
      window_sum += nums[i]

max_sum = window_sum
for i in range(k, len(nums)):
      window_sum = window_sum - nums[i-k] + nums[i]
      
      if window_sum > max_sum:
            max_sum = window_sum
print(max_sum/k)                                         