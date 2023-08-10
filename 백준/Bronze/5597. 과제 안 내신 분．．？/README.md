# [Bronze V] 과제 안 내신 분..? - 5597 

[문제 링크](https://www.acmicpc.net/problem/5597) 

### 성능 요약

메모리: 31256 KB, 시간: 44 ms

### 분류

구현

### 문제 설명

<p>X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.</p>

<p>교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.</p>

### 출력 

 <p>출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.</p>

### 오답노트.. 

1. 내 틀린 코드 <- 왜 .. 틀렷을까 ..
  
```python
arr = [] # 항상 배열 초기화 기억하기!!
for i in range(28): 
  arr.append(int(input())) #append 사용하기!
arr.sort()
nsub = []

for i in range(1, 30):
  #if arr[i] != i: 이케 쓰면 일치하지 않는 부분부터 쭉 걸림
   if i not in arr: #챗씨의 의견 .. 굳.. 
    nsub.append(i)
nsub.sort()
print(nsub[0])
print(nsub[1])
```
   
2. 정답코드 (1)
 ```python
students = [i for i in range(1,31)]

for _ in range(28):
    applied = int(input())
    students.remove(applied) #소거

print(min(students))
print(max(students))
```

3. 정답코드 (2)
   ```python
   import sys

students = [0 for i in range(30)]

for i in range(28):
    student_idx = int(sys.stdin.readline())
    students[student_idx-1] = student_idx
    
for i in range(2):
    idx = students.index(0)
    print(idx+1)
    students[idx] = -1
    ```
4. 정답코드(3)
```python
students = [i for i in range(1,31)]
for _ in range(28):
    s.remove(int(input()))
print(*students,sep="\n")
```
