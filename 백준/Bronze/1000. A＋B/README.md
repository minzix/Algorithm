# [Bronze V] A+B - 1000 

[문제 링크](https://www.acmicpc.net/problem/1000) 

### 성능 요약

메모리: 31256 KB, 시간: 44 ms

### 분류

구현, 사칙연산, 수학

### 문제 설명

<p>두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)</p>

### 출력 

 <p>첫째 줄에 A+B를 출력한다.</p>

***

### 내용 정리

```python
A, B = input().split()
print(int(A)+int(B))
```

1. `.split()` 함수
   * 다양한 형태로 사용이 가능함
     * 문자열.`split('구분자', 분할횟수)`: '구분자'를 기준으로 '분활횟수'만큼 나뉜다.
       '분할횟수'개수만큼의 원소가 생긴다.  
     * 문자열.split(): space, enter를 구분자로 삼으며 최대한 분할할 수 있는 만큼 나눈다.
       * 예)
         ```python
         s = "a b c d e f g"
         print(f's         : {s}') # 출력결과: a b c d e f g
 
         r = s.split()
         print(f's.split() : {r}') # 출력결과: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
         
         s = "aa.bb.cc.dd.ee.ff.gg"
         print(f's                : {s}') # 출력결과: 'aa.bb.cc.dd.ee.ff.gg'
         ```

2. `input()` 함수
   * 사용자로부터 입력을 받는 함수이다.
   * `무조건 문자열로 저장`되므로, 다른 형태로 바꾸고 싶다면 int(), float()등의 타입변환함수들을 사용해야한다. 
  
3. `int()` 함수
   * int형식으로 바꾸어준다.
