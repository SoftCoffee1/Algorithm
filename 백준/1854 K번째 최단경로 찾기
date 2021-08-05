# 1854 K번째 최단경로 찾기
# https://www.acmicpc.net/problem/1854

# 다익스트라 알고리즘은 최단경로가 찾아진 노드에 대해서는 다시 힙에 집어넣어서 탐색하지 않는다. 더 집어넣어봤자 최단경로를 구하는 과정에 도움이 되는 것이 아니므로!
# 만약, 더 집어넣게 되어 같은 노드를 또 한번 방문했을 때에 얻게도는 경로의 길이는, 두번째 최단경로가 된다.
# 이렇듯, k번째 최단경로가 찾아지기 전까지 계속 다시 힙에 노드와 거리를 집어넣어주게 되면, k번째 최단경로를 찾을 수 있게 된다.

# dp[i][j] (i번 노드의 j+1번째 최단경로) 를 설정하여, i번 노드에 도달 했을 시, dp[i][k-1] 즉 dp[i]의 최댓값과 현재 얻게된 경로를 비교하여, 최댓값보다 작으면 1 < ?? < k 번째 최단경로이므로,
# dp[i][k-1]에 넣어주기 정렬을 해주면 계속적으로 dp[i][k-1]는 i번째 노드로 가는 경로의 최댓값을 저장하고 있게 된다.

# 결과적으로 dp에는 k번째 이하의 최단경로의 정보가 모두 들어가있다. k번 미만으로 도달하게 되는 경우에는 dp[i]의 마지막 원소가 무한대로 설정되어 있을 것이다!


###### 들게 된 의문점!
# --------> i번 노드를 k+1번 방문하게 되어 다시 힙에 삽입하지 않게 되었다고 생각하자.
#           그런데, i번 노드를 통해 갈 수 있는 노드 중에서 i번 노드를 k+1번 이상 방문한 경로를 지나야만 k번째 최단경로를 찾을 수 있는 상황이 있을 수도 있는 것이 아닐까??
#
#          answer : 그런 상황은 존재하지 않는다. a --> .. --> b 가 되는 상황을 생각해보자. 이렇게 되면 아무리 못해도 a에 도달하게 된 횟수만큼 b에도 도달하게 된다.
#                   또한, a를 통한 경로가 아닌 제 3의 경로를 통해 b로 오게 되는 상황이 있을 수도 있다. 이 말은, a에 k+1번 도달하게 되는 상황은, 이미 b는 a를 통해 k번 도달하였고, 다른경로를 통해
#                   음이 아닌 정수 x번 더 도달했을것이 분명하다. 즉, a로부터 연결될 수 있는 노드들은 a를 k번 이하로 거쳐간 상황에서만 k번재 최단경로를 찾을 수 있게 되는 것이다.
#           

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k = map(int, input().rstrip().split())

graph = [{} for _ in range(n+1)]
for _ in range(m):
    v1, v2, d = map(int, input().rstrip().split())

    if v2 in graph[v1]:
        graph[v1][v2] = min(graph[v1][v2], d)

    else:
        graph[v1][v2] = d

# dp[i][j] : i번 노드의 j+1번째 최단경로!
dp = [[INF for _ in range(k)] for _ in range(n+1)]

# 1번 노드의 1번째 최단경로는 항상 0이다!
dp[1][0] = 0


queue = []
heapq.heappush(queue, (dp[1][0], 1))

while queue:
    curCost, here = heapq.heappop(queue)

    for there in graph[here]:
        nextCost = graph[here][there]

        # 새로운 경로의 길이
        now = curCost + nextCost

        # 의문점이 들게 된 파트!
        if now < dp[there][k-1]:
            dp[there][k-1] = now
            dp[there].sort()
            heapq.heappush(queue, (now, there))


# k번째 최단경로를 출력
for i in range(1,n+1):
    if dp[i][k-1] == INF:
        print(-1)
    else:
        print(dp[i][k-1])
