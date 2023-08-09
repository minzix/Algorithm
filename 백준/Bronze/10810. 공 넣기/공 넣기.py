# M번 공을 넣음
# i, j, k: i번 바구니부터 j번 바구니까지 k번 번호가 적힌 공을 넣음
# 예) 2 5 6: 2번 바구니부터 5번 바구니까지 6번 공을 넣음
# 바구니, 공의 번호 최댓값은 N임. 

N, M = map(int, input().split())
arr = [0] * N #원소가 0이고 원소의 개수가 N개인 배열 arr만들기
for a in range(M): 
  i, j, k = map(int, input().split())
  while i <= j:
    arr[i-1] = k #i-1을 빼먹음 ... 인덱스 정신차려
    i += 1 
for b in range(N): 
  print(arr[b], end = " ")