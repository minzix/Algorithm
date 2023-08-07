t = int(input())

for i in range(1, t+1):  # 1부터 t까지
    a, b = map(int, input().split())
    c = a + b
    print(f'Case #{i}: {a} + {b} = {c}')
    #Case #1: 1 + 1 = 2