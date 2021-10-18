def solution(N, number):
    dp = []
    str_n = str(N)
    # 9이상은 -1출력하므로 9개의 빈 배열
    for _ in range(9):
        dp.append([])
    #사칙연산 
    oper = ['+','-','//','*']
    #배열마다 해당 숫자만큼 붙인값 넣기 예)2->22
    for i in range(1,9):
        dp[i].append(int(str_n*i))
    #1번 배열이 number와 같으면 return 1
    if number in dp[1]:
        return 1
    #2번부터 8번까지
    for k in range(2,9):
        #예) N이 7일 경우
        #dp[1]연산dp[6] dp[2]연산dp[5] dp[3]연산dp[4]해야함
        #h의 범위 1,2,3
        for h in range(1,k//2+1):
            for a in dp[k-h]:
                for b in dp[h]:
                    for i in oper:
                        #두 수중 큰 수가 앞에와야 나눗셈,뺄셈가능
                        rr = eval(str(max(a,b))+i+str(min(a,b)))
                        if rr != 0 :
                            dp[k].append(rr)
        #답이 나오면 return k
        if number in dp[k]:
            return k
    #8개까지 구하고도 없으면 -1 return 
    return -1

print(solution(5,5555))