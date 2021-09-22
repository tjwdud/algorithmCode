#화성탐사
import heapq
INF = int(1e9)
t = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = []

def dijikstra(graph,distance):
    #출발 위치
    x,y = 0,0
    q = []
    n = len(graph)
    #출발지점 우선순위 큐에 넣는다.
    heapq.heappush(q,(graph[x][y],x,y))
    #나에서 나로 가는비용 
    distance[0][0] = graph[0][0]
    while q:
        #큐가 존재할때까지 꺼내
        dist,x,y= heapq.heappop(q)
        #꺼낸것의 거리가 지금 거리보다도 크면 무시(이미 처리된적 있는 노드라면 무시)
        if dist > distance[x][y]:
            continue
        #사방 탐사 지금의 나와 연결되어 있는 노드 확인
        for i in range(4):
            now_x = x + dx[i]
            now_y = y + dy[i]
            #범위 넘어가면 무시
            if now_x <= -1 or now_y <= -1 or now_x >= n or now_y >=n:
                continue
            #큐에 있는 현재 노드를 거쳐 가는 비용을 계산
            cost = dist + graph[now_x][now_y]
            #계산한 비용이 지금 거리보다 작으면 바꿈
            if cost < distance[now_x][now_y]:
                distance[now_x][now_y] = cost
                heapq.heappush(q,(distance[now_x][now_y],now_x,now_y))
    return distance[n-1][n-1]

for _ in range(t):
    n = int(input())
    graph = []
    distance = [[INF] * (n) for _ in range(n)]
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    result.append(dijikstra(graph,distance))

for i in result:
    print(i)
'''
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''