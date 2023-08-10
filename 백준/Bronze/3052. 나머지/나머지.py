arr = []
for i in range(10): 
  arr.append(int(input())%42)

res = 10
print(len(set(arr)))


# for i in range(0, 8): 
#   if arr[i] == arr[i+1]: 
#     res -= 1
# print(res)