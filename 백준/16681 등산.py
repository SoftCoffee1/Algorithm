# 16681 등산
# https://www.acmicpc.net/problem/16681


## 기본적인 다익스트라에서, 오르막길만을 선별해서 최단경로를 체크해야 하는 간단한 문제였다.
## 집으로부터의 오르막길, 고려대학교로부터의 오르막길을 구해야 하는 문제로, 총 2번의 다익스트라를 사용하면 된다.

import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize


def dijkstraFrom(start):
    global graph
    global height
    global N
    
    dist = [INF for _ in range(N+1)]
    queue = []

    dist[start] = 0
    heapq.heappush(queue, (dist[start], start))

    while queue:
        nowCost, here = heapq.heappop(queue)

        ## 최단경로가 이미 발견 된 경우, 무시하기!
        if dist[here] < nowCost:
            continue


        for there in graph[here]:

            ## 새로운 높이가 현재 높이보다 높지 않다면 무시하기!
            if height[there] <= height[here]:
                continue

            
            nextCost = graph[here][there]

            now = nowCost + nextCost
            
            if dist[there] > now:
                dist[there] = now
                heapq.heappush(queue, (dist[there], there))


    return dist

            
           

## 지점의 개수, 경로의 개수, 1초당 체력 소모량, 높이 1당 성취감
N, M, D, E = map(int, input().rstrip().split())


## 지점들의 높이(인덱스가 곧 지점의 번호)
height = [0]+list(map(int, input().rstrip().split()))


## 그래프 초기화(두 지점을 잇는 경로가 여러가지)
graph = [{} for _ in range(N+1)]
for _ in range(M):
    a, b, n = map(int, input().rstrip().split())

    if b in graph[a]:
        graph[a][b] = min(graph[a][b], n)

    else:
        graph[a][b] = n


    if a in graph[b]:
        graph[b][a] = min(graph[b][a], n)

    else:
        graph[b][a] = n




home = dijkstraFrom(1)
school = dijkstraFrom(N)


result = -INF
for i in range(2,N):
    length = home[i] + school[i]

    if length > INF:
        continue
    
    cur = height[i] * E - (home[i] + school[i]) * D

    result = max(result, cur)


if result != -INF:
    print(result)

else:
    print("Impossible")
