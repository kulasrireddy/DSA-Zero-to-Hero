# #Best time to buy and sell shock
prices = list(map(int, input().split()))
min_prices = prices[0]
max_profit = 0
for price in prices:
      if price < min_prices:
            min_prices = price
      profit = price - min_prices
      if profit > max_profit:
            max_profit = profit
print(max_profit)           

#Majority Element
nums = list(map(int, input().split()))
freq = {}
for num in nums:
      if num in freq:
            freq[num] += 1
      else:
            freq[num] = 1
for key, val in freq.items():      
      if val > len(nums) // 2:
            print(key)          

#Majority element - boyer moore voting algorithm
nums = list(map(int, input().split()))
cand = None
count = 0
for num in nums:
      if count == 0:
            cand = num
      if  num == cand:
            count += 1
      else:
            count -= 1
print(cand)                        
