def solution(triangle):
    #memoization을 위한 depth
    depth = []
    #triangle 길이 만큼 빈배열로 초기화
    for _ in range(len(triangle)):
        depth.append([])
    depth[0].append(triangle[0][0])
    for i in range(1,len(triangle)):
        for j in range(i+1):
            #맨 왼쪽은 전  depth[전단계][0]에서 현재 triangle더하기
            if j == 0:
                depth[i].append(depth[i-1][0]+triangle[i][j])
            #맨 오른쪽은 depth[전단계][j-1]에서 현재 triangle더하기
            elif j == i:
                depth[i].append(depth[i-1][j-1]+triangle[i][j])
            #중간인 경우 depth[전단계][j-1]과 depth[전단계][j] 중에 큰 수를 현재 triangle에 더하기
            else:
                depth[i].append(max(depth[i-1][j-1],depth[i-1][j])+triangle[i][j])
    #가장 아래층에서 가장 큰수 구해서 return
    return max(depth[len(depth)-1])
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

