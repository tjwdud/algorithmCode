INF = int(1e9)
def solution(n, results):
    answer = 0
    graph = [[INF] * (n+1) for _ in range(n+1)]
    for a,b in results:
        graph[a][b] = 1
    #자기자신으로 가는경우 0
    for a in range(1, n+1):
        for b in range(1,n+1):
            if a == b:
                graph[a][b] = 0
    #해당 노드로 오거나 갈수있으면 순위비교가 가능한것
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                graph[a][b] = min(graph[a][k]+graph[k][b],graph[a][b])
    count = 0
    for i in range(1,n+1):
        count = 0
        for j in range(1, n+1):
            #해당 노드로 오거나 갈 수 있으면 순위비교 가능
            if graph[i][j] != INF or graph[j][i] != INF:
                count += 1
        if count == n:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))