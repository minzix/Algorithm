def solution(participant, completion):
    dic = {}
    sumPartHash = 0
    for i in participant: 
        dic[hash(i)] = i
        sumPartHash += hash(i)
    for i in completion: 
        sumPartHash -= hash(i)
    # 결론적으로 sumPartHash를 key로 가지는 value를 dic에서 가져와야함
    return dic[sumPartHash]

# 참가자 중에는 동명이인이 있을 수 있습니다 - 이 문장이 모든 문제의 시발점임.. 얘만 없으면
'''
def solution(participant, completion):
    participant_set = set(participant)
    completion_set = set(completion)
    answer = participant_set - completion_set
    return answer
'''
# 걍 이케 써서도 가능.. 그치만 여기선 set 사용 안됨 ㅜ
