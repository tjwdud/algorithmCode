INF = int(1e9)

#노드의 갯수 간선의 갯수 입력받기
n = int(input())
m = int(input())

#2차원 리스트를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신으로 가는 경우는 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print('무한')
        else:
            print(graph[a][b], end=" ")
    print()

