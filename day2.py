# #Check an array is sorted or not
# nums = list(map(int, input().split()))
# if len(nums) <= 1:
#       print("True")
# else:
#       for num in range(len(nums) - 1):
#             if nums[num] > nums[num + 1]:
#                   print("False")
#                   break
#       else:
#             print("True")         
            


arr = list(map(int, input().split()))
target = int(input()) 
for i in range(len(arr)):
      if arr[i] == target:
            print(i)
            break
else:
      print(-1)        