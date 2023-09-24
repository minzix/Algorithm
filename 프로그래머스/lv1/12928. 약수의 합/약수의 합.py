def solution(n):
    answer = 0
    for i in range(1, n + 1): # ZeroDivisionError 방지
        if n % i == 0: 
            answer = answer + i 
    return answer