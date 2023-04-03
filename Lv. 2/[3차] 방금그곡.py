def TimetoNum(time):
    return int(time.split(":")[0]) * 60 + int(time.split(":")[1])

def ChangeMusic(music):
    change = {"C#" : "1", "D#" : "2", "F#": "3", "G#": "4", "A#" : "5"}
    for before, after in change.items():
        music = music.replace(before, after)
    
    return music        
        
def solution(m, musicinfos):
    answer = ''
    
    temp_playTime = 0
    
    for musicinfo in musicinfos:
        infos = musicinfo.split(",")
        playTime = TimetoNum(infos[1]) - TimetoNum(infos[0])
        
        music = ChangeMusic(infos[3])
        
        rep = playTime // len(music) + 1
        
        if ChangeMusic(m) in (music * rep)[:playTime] and playTime > temp_playTime:
            temp_playTime = playTime
            answer = infos[2]                    
    
    if answer == '':
        return "(None)"
    
    return answer