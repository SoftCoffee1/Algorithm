# 1162 도로포장
# https://www.acmicpc.net/problem/1162

# 다차원 다익스트라문제이다.

# 1. 그냥 최소시간이 아닌, K개 이하의 도로를 포장하면서 최소 시간을 구하는 문제이다.
# 2. 최단경로를 택하여 그 경로에서 큰 원소부터 K개를 제거하는 아이디어는 불가능하다.
# 3. 그래서 매번 다음 도시를 갈때 그 도시를 포장할지 안할지를 둘다 체크하면서 가야하는 문제이다.

# 4. K개 이하의 도로를 포장하라고 한 이유는 실제 최단경로는 K개 이상의 도로 구성되어 있어,
#    K개의 도로를 포장해도 양수의 시간이 걸린다. 그러나 어떤 경로중 K개 미만의 도로로 구성되어 있다면, K개 이하의 도로를 사용하여 시간이 0이 걸리며 도착지점에 도달할 수 있기 때문이다.

# 카카오 2020 인턴십 "경주로 건설" 문제로 유사한 부분이 있는 문제이다.


import heapq
import sys
input = sys.stdin.readline
INF = int(1e12)

N, M, K = map(int, input().rstrip().split())

graph = [{} for _ in range(N+1)]
for _ in range(M):
    a, b, d = map(int, input().rstrip().split())

    if b in graph[a]:
        graph[a][b] = min(graph[a][b], d)

    else:
        graph[a][b] = d


    if a in graph[b]:
        graph[b][a] = min(graph[b][a], d)

    else:
        graph[b][a] = d


### 문제의 핵심!!
# dp[city][k] : city까지 k개의 도로를 포장하여 도달할 수 있는 최소시간
dp = [[INF for _ in range(K+1)] for _ in range(N+1)]

# 1번 도시까지 도달할 수 있는 최소 시간은 0이므로 그렇게 초기화 해주기!
for i in range(K):
    dp[1][i] = 0

# queue는 (걸리는 시간, 도시번호, 포장도로 개수) 를 원소로 갖는다.
queue = []
heapq.heappush(queue, (0, 1, 0))


while queue:
    nowCost, nowCity, pavedRoad = heapq.heappop(queue)

    # 다익스트라 작동 과정 중 최솟값보다 큰 경우 무시하기!
    if dp[nowCity][pavedRoad] < nowCost:
        continue


    for nextCity in graph[nowCity]:
        nextCost = graph[nowCity][nextCity]


        # 다음 도시로 갈때 다음도시를 포장을 안하고 가는 경우
        if dp[nextCity][pavedRoad] > nowCost + nextCost:
            dp[nextCity][pavedRoad] =  nowCost + nextCost
            heapq.heappush(queue, (dp[nextCity][pavedRoad], nextCity, pavedRoad))


        # 다음 도시로 갈때 다음도시를 포장하고 가는 경우
        if pavedRoad < K:
            if dp[nextCity][pavedRoad + 1] > nowCost:
                dp[nextCity][pavedRoad+1] =  nowCost
                heapq.heappush(queue, (dp[nextCity][pavedRoad+1], nextCity, pavedRoad+1))


# K개의 도로를 포장할 수가 없는 경우도 존재할 수 있으므로 (위의 4번에 설명 써놓음) dp[N][K]를 출력하는 것이 아닌 min(dp[N])를 출력해야 한다.
print(min(dp[N])
