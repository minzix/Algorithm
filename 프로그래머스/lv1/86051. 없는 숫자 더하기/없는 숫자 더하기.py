def solution(numbers):
    vacant = []
    for i in range(10):
        if i not in numbers: 
            vacant.append(i)
    answer = sum(vacant)
    return answer

# 0~9까지의 숫자를 배열 numbers 의 원소와 하나씩 비교해 같은 수가 없으면 다른 배열에 저장하기
# 배열의 원소 전체 합 구하기 -> 배열.sum()