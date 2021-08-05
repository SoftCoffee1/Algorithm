# 1504 특정한 최단 경로
# https://www.acmicpc.net/problem/1504


# 특정 정점을 통과하며 도착점에 도달해야 하는데, 갔던 점은 다시 도달 가능!

# 1. 다익스트라 알고리즘을 여러번 사용하는 문제! 함수로 만들어 놓기 & 다익스트라의 기본적인 프로토타입 점검하기!
# 2. 무향 그래프의 경우, a -> b의 길이는 b -> a와 같음을 생각하면 다익스트라를 최소한으로 돌려서 필요한 최단경로들을 구할 수 있다.



import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    global graph
    global N

    dist = [INF for _ in range(N+1)]
    dist[start] = 0

    queue = []
    heapq.heappush(queue, (dist[start], start))


    while queue:
        curCost, here = heapq.heappop(queue)

        # 다익스트라 알고리즘의 이미 지나온 노드 무시하는 방법!
        # 두번째 이후부터 방문하는 경로의 길이는 최단경로보다는 무조건 길 것이므로, 그러한 것들은 무시하기!
        # <=가 안되는 이유는, 시작점의 경우 이 if문에 걸려 제대로 작동하지 않게 된다!
        if dist[here] < curCost:
            continue


        for there in graph[here]:
            nextCost = graph[here][there]

            if dist[there] <= curCost + nextCost:
                continue


            dist[there] = curCost + nextCost
            heapq.heappush(queue, (dist[there], there))


    return dist
    
    
    
    


N, E = map(int, input().rstrip().split())


# 그래프 초기화 과정!
# 두개의 정점을 잇는 간선이 여러개인 경우, 최소를 저장하는 스킬!
graph = [{} for _ in range(N + 1)]
for _ in range(E):
    v1, v2, d = map(int, input().rstrip().split())
    if v2 in graph[v1]:
        graph[v1][v2] = min(graph[v1][v2], d)
        graph[v2][v1] = min(graph[v2][v1], d)
    else:
        graph[v1][v2] = d
        graph[v2][v1] = d

v1, v2 = map(int, input().rstrip().split())

# v1, v2를 출발점으로 하는 모든 최단경로를 저장하는 리스트
startNode_v1 = dijkstra(v1)
startNode_v2 = dijkstra(v2)


v1_v2_N = startNode_v1[1] + startNode_v1[v2] + startNode_v2[N]
v2_v1_N = startNode_v2[1] + startNode_v1[v2] + startNode_v1[N]

result = min(v1_v2_N, v2_v1_N)

if result >= INF:
    print(-1)

else:
    print(result)

