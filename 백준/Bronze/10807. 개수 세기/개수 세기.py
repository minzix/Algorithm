N = int(input())
arr = list(map(int, input().split()))
v = int(input())
sum = 0
for i in range(N): 
    if arr[i] == v:
        sum += 1
print(sum)
        