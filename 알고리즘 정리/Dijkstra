# graph : 딕셔너리를 원소로 갖는 인접 리스트 형태의 그래프  --> 그냥 인접 리스트의 경우, 32, 33 번째 줄을 지우고 아래의 문장으로 수정해야 함!
#                                                                                    --->  for there, nextCost in graph[here]:
# N : 노드의 개수


def dijkstra(start):
    global graph
    global N
    
    # 최단경로를 저장할 배열 -> 노드번호가 곧 인덱스번호로 하기 위해 리스트 사이즈를 N+1로 함!
    dist = [INF for _ in range(N+1)]
    
    # 시작점까지의 거리는 0으로 초기화
    dist[start] = 0
  
    # 최소 힙을 사용하여 우선순위 큐를 구현
    queue = []
    heapq.heappush(queue, (dist[start], start))

    
    # 루프 시작!
    while queue:
        curCost, here = heapq.heappop(queue)

        # 다익스트라 알고리즘의 이미 지나온 노드 무시하는 방법!
        # 두번째 이후부터 방문하는 경로의 길이는 최단경로보다는 무조건 길 것이므로, 그러한 것들은 무시하기!
        # <=가 안되는 이유는, 시작점의 경우 이 if문에 걸려 제대로 작동하지 않게 된다!
        if dist[here] < curCost:
            continue

        # 각각의 인접 노드들에 대해서 확인하기
        for there in graph[here]:
            nextCost = graph[here][there]
            
            # 기존에 얻은 최단 경로보다 새롭게 만들어지는 경로의 길이가 큰 경우 무시한다!
            # 더 짧을 때만 업데이트 해야 최단경로를 구할 수 있기 때문이다.
            if dist[there] <= curCost + nextCost:
                continue

            
            # 여기까지 온 것은 최단경로를 업데이트 해야한다는 의미로,
            # 최단경로 업데이트를 하고
            # 큐에 현재까지의 최단겨로와, 노드번호를 넣어준다.
            # 최단경로가 앞에 오는 튜플을 형성해야 하는데, 최소 힙의 특성상 앞의 원소부터 체크하기 때문이다.
            dist[there] = curCost + nextCost
            heapq.heappush(queue, (dist[there], there))

    
    # start로부터 모든 노드까지의 최단경로를 저장하는 리스트를 반환
    return dist
