import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

#노드의 갯수 간선의 개수를 입력받기
n , m = map(int,input().split())
#시작 노드번호
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for _ in range(n+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())

    graph[a].append((b,c))

def dijkstra(start):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로
    heapq.heappush(q, (0, start))
    distance[start] = 0

    #큐가 비어있지 않다면
    while q:
        #최단 경로가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리된적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        #현재 노드와 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
    if distance[i] == INF:
        print("무한")
    else:
      print(distance[i])

'''
 6 11
 1
 1 2 2
 1 3 5
 1 4 1
 2 3 3
 2 4 2
 3 2 3
 3 6 5
 4 3 3
 4 5 1
 5 3 1
 5 6 2
 '''