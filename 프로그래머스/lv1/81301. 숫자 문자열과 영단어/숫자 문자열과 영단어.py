def solution(s):
    table = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    for key, value in table.items(): # dictionary.items() : 사전의 키, 아이템 얻기
        s = s.replace(key, value) # replace(a, b) : a를 b로 대체

    return int(s)