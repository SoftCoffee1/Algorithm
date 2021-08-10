#2211 네트워크 복구
# https://www.acmicpc.net/problem/2211

# 다익스트라를 활용하여, 시작점과 모든점들이 최소 개수의 간선, 간선길이의 총합의 최소를 갖는 간선들을 출력!
# 최소 스패닝 트리느낌이 나지만, 시작점이 정해져 있으므로, 그렇게 풀 수 없다!

# 다익스트라를 풀때 visited 배열을 활용하면 조금더 빠르지만 메모리 조금 더 차지!

# visited 배열을 사용하지 않으려면, 초기화과정에서
#  ------------------> 1. 시작점을 힙에 추가
#  ------------------> 2. 시작점까지의 거리 0으로 초기화
# --> 이렇게 두개의 과정을 처리해주어야함!!


import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().rstrip().split())


# 서로 다른 두점을 직접적으로 잇는 선이 두개 이상인 경우에 가장 최소만 취하는 방법!
graph = [{} for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().rstrip().split())

    if B in graph[A]:
        graph[A][B] = min(graph[A][B], C)

    else:
        graph[A][B] = C


    if A in graph[B]:
        graph[B][A] = min(graph[B][A], C)

    else:
        graph[B][A] = C


distance = [INF for _ in range(N+1)]
#visited = [False for _ in range(N+1)] --> 시작점 초기화는 할 필요 없다!


# 복구할 회선 저장할 배열
result = []


# (time, node) 를 저장하는 우선순위 큐
queue = []

# 힙에 추가하고,
# 시작점거리 0으로 초기화 해주기! --> 이러면 visited 배열 필요없다!
heapq.heappush(queue, (0,0,1))
distance[1] = 0


while queue:
    totalTime, cameFrom, here = heapq.heappop(queue)


    # here에 도착한 새로운 시간(totalTime) 이 최소시간보다 큰 경우 무시하기!
    if distance[here] < totalTime:
        continue

    # visited 배열 있을때 하는 방법!
    """
    if visited[here]:
        continue
    
    visited[here] = True
    """

    # 시작점이 아닌 경우 간선에 추가!
    if cameFrom != 0:
        result.append((cameFrom, here))


    for there in graph[here]:
        lineTime = graph[here][there]


        if distance[there] > totalTime + lineTime:
            distance[there] = totalTime + lineTime
            heapq.heappush(queue, (distance[there], here, there))

# 간선의 개수 출력
print(len(result))

# 간선의 형태 모두 출력
for a, b in result:
    print(a,b)
    
