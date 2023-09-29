def solution(numbers):
    vacant = []
    for i in range(10):
        if i not in numbers: 
            vacant.append(i)
    answer = sum(vacant)
    return answer