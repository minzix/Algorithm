def solution(a, b):
    answer = 0
    if a % 2 != 0 and b % 2 != 0: # 모두 홀수
        answer = a ** 2 + b ** 2
    elif a % 2 == 0 and b % 2 == 0: # 모두 홀수가 아님
        if a - b < 0: 
            answer = -(a - b)
        else: answer = a - b
    else: 
        answer = 2 * (a + b)
    return answer