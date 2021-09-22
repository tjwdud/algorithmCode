import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

n,m,c = map(int,input().split())
graph = [[] for _ in range(1+n)]
distance = [INF] * (n+1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstart(start):
    q = []
    distance[start] = 0

    heapq.heappush(q,(0,start))

    while q:
        dist,now = heapq.heappop(q)
        #처리된 적이 있으면 다음꺼 꺼내
        if dist > distance[now]:
            continue
        for i in graph[now]:
            #지금 노드와 연결되어있는 노드의 거리가 
            #힙에서 꺼낸 노드의 거리 + 한번에 가는 거리
            if distance[i[0]] > dist+i[1]:
                distance[i[0]] = dist+i[1]
                heapq.heappush(q,(dist+i[1],i[0]))






