# 도착방향까지 고려해주어야 하는 다익스트라 문제

# 1. 다익스트라의 기본 포맷은 유지하되
# 2. 방향이라는 변수가 하나 추가되었을 뿐인 문제이다.
# 3. 여러 cost로 특정 지점에 도달했다 하더라도 그 방향에 따라 결과값이 달라질 수 있기 때문이다.



import heapq

def solution(board):
    INF = int(1e9)

    N = len(board)

    # 머리방향
    # 0 : 3시
    # 1 : 6시
    # 2 : 9시
    # 3 : 12시
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    ##### 이 문제의 핵심!!  #########
    # dist[x][y][head] : (x,y) 위치에 머리방향이 head로 도착했을 때의 최소 견적을 저장하는 3차원 리스트
    dist = [[[INF for _ in range(4)] for _ in range(N)] for _ in range(N)]

    

    # queue : (거리, x, y, 머리방향) 을 저장한다.
    queue = []

    # 초기위치에서는 3시방향, 6시방향으로 밖에 진행하지 못한다!
    # 초기위치 초기화 후, 힙에 넣어주기
    dist[0][0][0] = 0
    dist[0][0][1] = 0
    heapq.heappush(queue, (dist[0][0][0], 0, 0, 0))
    heapq.heappush(queue, (dist[0][0][1], 0, 0, 1))
    


    while queue:
        nowCost, x, y, head = heapq.heappop(queue)


        # 현재 상태에 오기까지 필요한 지금까지의 최소견적이 지금 탐색중인 상황에서의 견적보다 작을 경우
        # 이미 최소가 발견된 것이므로 무시한다!
        if dist[x][y][head] < nowCost:
            continue


        # 4방향 모두 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            # 범위를 벗어나면 무시하기
            if not (0 <= nx < N and 0 <= ny < N):
                continue

            # 벽을 만나면 무시하기
            if board[nx][ny] == 1:
                continue
            

            # 머리방향이 같으면 100원 추가
            if i == head:
                nextCost = 100

            # 머리방향이 다르면 직선도로 100원 + 꺽이는 점 500원 = 600원을 추가
            elif i != head:
                nextCost = 600


            # (nx, ny)에 head 방향으로 도달 할 시 필요한 견적
            now = nowCost + nextCost

            # 그 견적이 현재까지의 최소견적보다 작을 시에 업데이트
            #### 2차원 배열을 활용해 풀이하려고 시도했을 때는, dist[nx][ny] == now 이더라도 다른방향으로 도달하는 경우 최솟값을 만들어낼 수 있는 가능성이 여전히 있으므로  >= 로 처리해줬었다.
            if dist[nx][ny][i] > now:
                dist[nx][ny][i] = now
                heapq.heappush(queue, (dist[nx][ny][i], nx, ny, i))
                

    # (N-1, N-1) 에 도달할 수 있는 경로가 2가지(3시방향, 6시방향)인데, 그중에 더 작은 값이 답이 된다!
    return min(dist[-1][-1])
