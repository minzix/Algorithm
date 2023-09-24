def solution(n):    
    answer = 0
    n = str(n)
    for i in range(len(n)): 
        answer = answer + int(n[i])
    return answer

"""
def solution(n):    
    answer = 0
    arr = []
    arr = list(n.split('')) -> 숫자를 split 해서 배열에 저장하고 sum 하고 싶었음,, 
    answer = sum(arr)
    return answer
"""
