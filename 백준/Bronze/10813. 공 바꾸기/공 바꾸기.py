# 바구니에 공 하나씩 들어있음
# 공과 바구니의 번호 같음
# N: 바구니 번호 max
# M: 바구니 교환 횟수

N, M = map(int, input().split())
arr = list(range(1, N+1))  # 1부터 N까지의 숫자로 배열 초기화(내가 놓친 부분!!)


for a in range(N): 
  arr[a] = a+1
#print(arr)

for b in range(M): 
  i, j = map(int, input().split())
  temp = arr[i-1]
  arr[i-1] = arr[j-1]
  arr[j-1] = temp
  #print(arr)

for c in range(N): 
  print(arr[c], end = " ")