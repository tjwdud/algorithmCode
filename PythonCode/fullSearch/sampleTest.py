def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    thr = [3,3,1,1,2,2,4,4,5,5]
    scores = [0,0,0]
    for i in range(len(answers)):
        if one[i%len(one)] == answers[i]:
            scores[0] += 1
        if two[i%len(two)] == answers[i]:
            scores[1] += 1
        if thr[i%len(thr)] == answers[i]:
            scores[2] += 1
    for i in range(3):
        if scores[i] == max(scores):
            answer.append(i+1)
    return answer
