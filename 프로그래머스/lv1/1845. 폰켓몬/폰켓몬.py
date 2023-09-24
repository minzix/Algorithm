def solution(nums):
    answer = 0
    # 중복된 수를 제거한 배열을 추출
    unique_nums = list(set(nums))
    
    if len(unique_nums) > len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(unique_nums)
    return answer

# 1. 배열 nums에서 중복되는 수를 제거한 배열을 추출해야함 -> list(set(nums)) 이용
# 2. 추출한 배열의 수가 len(nums) 보다 더 크면 answer = len(nums)/2
# 3. 작으면 answer = 배열의 수