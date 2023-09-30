def solution(players, callings):
    # list를 map하는 과정 -> players를 딕셔너리로 만듦
    # maps(딕셔너리이름) = {키로 지정하고 싶은 것 : 값으로 지정하고 싶은 것 for 키, 값 in enumerate(리스트이름)}
    maps = {player: idx for idx, player in enumerate(players)}

    # for loop callings list
    for player in callings:
        # 현재 호출된 유저의 순위(인덱스) curPlayer에 할당
        curPlayer = maps[player]
        # maps에 저장된 현재 호출된 유저 순위 -1
        maps[player] -= 1
        # maps에 저장된 호출된 유저의 앞에 있던 유저 순위 +1
        maps[players[curPlayer-1]] += 1
        # players list에 저장된 두 유저의 위치 교체
        temp = players[curPlayer]
        players[curPlayer] = players[curPlayer - 1]
        players[curPlayer - 1] = temp

    return players
    """
    1M * 50K
    50 G - 500억 -> 일반 완전탐색 불가능
    callings은 결국 다 순회 해야 합니다 -> 최소 순회 1M
    그렇다면 앞서 플레이어는 한 번만 순회하면 어떨까?
    플레이어를 map에 모두 저장, 키를 플레이어로, 값을 현재 순위로 저장 (결국 순위는 리스트의 인덱스입니다.)
    순위를 1위, 2위로 기록할 필요가 없기 때문에 인덱스 + 1을 할 필요는 없습니다.
    callings를 순회
    현재 호출된 플레이어의 순위를 저장하고
    map에 저장된 현재 플레이어의 순위를 1등 올리고(실제 연산은 -1)
    map에 저장된 앞선 플레이어의 순위를 1등 내려줍니다.(실제 연산은 +1)
    maps[players[curPlayer-1]] += 1
    players[curPlayer-1]는 결국 현재 유저의 앞선 유저의 순위(인덱스)를 참조해서 해당 앞선 유저의 이름을 찾고
    그 이름을 key로 maps에서 앞의 유저를 찾아낸 후, 순위를 변경하는 코드입니다.
    이후, 실제 players 배열에서 두 플레이어의 위치를 교환
    players 반환
    """