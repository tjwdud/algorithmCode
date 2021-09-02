def solution(table, languages, preference):
    answer = ''
    score = []
    lan_idx = 0
    max_score = []
    qq = []
    for i in table:
        score = []
        for k in languages:
            if k in i.split():
                score.append((6 - i.split().index(k))*preference[lan_idx % len(languages)])
            else:
                score.append(0)
            lan_idx += 1
        max_score.append(sum(score))

    result = max(max_score)
    new_co = [i for i, ele in enumerate(max_score) if ele == result]
    print(new_co)
    dic = {0 :'SI',1:'CONTENTS',2:'HARDWARE',3:'PORTAL',4:'GAME'}
    for i in new_co:
        qq.append(dic[i])
    answer = sorted(qq)[0]
    return answer