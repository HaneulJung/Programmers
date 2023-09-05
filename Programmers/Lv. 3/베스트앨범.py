# 장르별 가장 많이 재생된 노래 2개씩 모아 베스트 앨범 출시
# 노래는 고유 번호로 구분
# 속한 노래가 많이 재생된 장르 먼저 수록
# 장르 내 많이 재생된 노래 먼저 수록, 만약 재생 횟수 같으면 고유 번호 낮은 노래 먼저 수록
    
def solution(genres, plays):
    answer = []
    n = len(genres)
    
    songs = {}
    playCnt = {}
    
    for i in range(n):
        if genres[i] not in songs.keys():
            songs[genres[i]] = [(i, plays[i])]
            playCnt[genres[i]] = plays[i]
        else:
            songs[genres[i]].append((i, plays[i]))
            playCnt[genres[i]] += plays[i]
            
    for genre in sorted(playCnt, key=lambda x : playCnt[x], reverse=True):
        songs[genre].sort(key=lambda x : (-x[1], x[0]))
        try:
            answer.append(songs[genre][0][0])
            answer.append(songs[genre][1][0])
        except:
            pass
    
    return answer