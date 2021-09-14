INF = int(1e9)
n , m =map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

#자신으로 가는것 0으로 초기회
for a in range(1,n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1

x, k = map(int,input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for n in range(1, n+1):
            graph[a][b]= min(graph[a][b], graph[a][k]+graph[k][b])
            graph[b][a] = min(graph[a][b], graph[a][k]+graph[k][b])


if graph[1][k]+graph[k][x] >= INF:
    print(-1)
else:
  print(graph[1][k]+graph[k][x])
'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''