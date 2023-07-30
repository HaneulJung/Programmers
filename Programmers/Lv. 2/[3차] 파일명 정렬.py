def solution(files):
    answer = []
    
    dic = {}
    
    
    for file in files:
        head = ''
        number = ''
        isDig = False
        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
                isDig = True
            else:
                if isDig:
                    dic[file] = [head, int(number)]
                    break
                else:
                    head += file[i].lower()
        if file not in dic.keys():
            dic[file] = [head, int(number)]
    
    answer = sorted(dic, key=lambda x : (dic[x][0], dic[x][1]))
    
    return answer