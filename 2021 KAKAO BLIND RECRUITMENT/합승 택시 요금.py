import heapq

def dijkstra(start, n):
    global graph

    INF = int(1e9)
    
    dist = [INF for _ in range(n+1)]
    dist[start] = 0
    
    queue = []
    heapq.heappush(queue, (dist[start], start))


    while queue:
        cost, nowNode = heapq.heappop(queue)

        ## 이미 더 작은 경로가 발견 되었다면 무시하기
        if dist[nowNode] < cost:
            continue


        for nextNode in graph[nowNode]:
            nextCost = graph[nowNode][nextNode]

            totalCost = cost + nextCost

            ## 현재 탐색 경로의 비용이 더 작은 경우
            if totalCost < dist[nextNode]:
                dist[nextNode] = totalCost
                heapq.heappush(queue, (dist[nextNode], nextNode))


    return dist

    


def solution(n, s, a, b, fares):
    global graph

    INF = int(1e9)

    graph = [{} for _ in range(n+1)]
    for c, d, f in fares:

        if d not in graph[c]:
            graph[c][d] = f

        else:
            graph[c][d] = min(graph[c][d], f)

        if c not in graph[d]:
            graph[d][c] = f

        else:
            graph[d][c] = min(graph[d][c], f)


    ## 모든 지점을 경유의 대상으로 보고,
    ## 경유 지점에서의 한번의 다익스트라를 통해 그상황에서의 요금 구해서
    ## 최솟값을 구하기!
    answer = INF
    for via in range(1, n+1):

        dist = dijkstra(via, n)
        
        current_cost = dist[s] + dist[a] + dist[b]

        if answer > current_cost:
            answer = current_cost

        
    
    return answer
