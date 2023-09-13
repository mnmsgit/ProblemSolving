def solution(players, callings):
    ranking = dict()
    for i in range(len(players)):
        ranking[players[i]] = i
        
    for call in callings:
        now = ranking[call]
        prev_player = players[now-1]
        players[now], players[now-1] = players[now-1], players[now]
        ranking[call] -=1
        ranking[prev_player] +=1
        
    return players