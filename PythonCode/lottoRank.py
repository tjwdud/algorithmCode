def solution(lottos, win_nums):
    zeroNum = 0;
    exepZero = [];
    bestScore = 6;
    worstScore = 6;
    score = [6,5,4,3,2,1]
    for i in lottos:
        if(i==0):
            zeroNum = zeroNum + 1
        else:
            exepZero.append(i)

    sameNum = list(set(exepZero) & set(win_nums))
    best = len(sameNum) + zeroNum
    worst = len(sameNum)

    for idx,num in enumerate(score):
          if(num == best):
              bestScore = idx+1
          if(num == worst):
              worstScore = idx+1

    answer = [bestScore, worstScore]
    return answer
print('fff')
print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))