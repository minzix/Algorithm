N = int(input())
arr = []
arr = list(str(input()))
sum = 0
for i in range(len(arr)): 
  sum += int(arr[i-1])
print(sum)