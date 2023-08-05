A, B, C = map(int, input().split())

# 모든 눈이 동일한 경우
if A == B == C: 
    M = 10000 + A * 1000 
# 두 눈이 동일한 경우
elif A == B or A == C or B == C:
    # 두 눈이 동일한 경우, 1,000을 더하고 눈의 값(A, B, 또는 C)을 100으로 곱해서 M에 더한다.
    if A == B or A == C: 
        M = 1000 + A * 100
    else:
        M = 1000 + B * 100
# 모든 눈이 다른 경우
else:
    M = max(A, B, C) * 100

print(M)