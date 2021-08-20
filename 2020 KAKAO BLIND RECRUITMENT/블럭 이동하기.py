## 다익스트라 아이디어를 사용하여 구현하였다.
## 이동하는 물체의 생김새가 특이한 문제였지만, 이동하는 것은 구현하는 것이 복잡하지는 않았다.
## 그러나, 물체가 회전하는 경우를 포함하는 문제여서, 그 부분에서 오류가 나서 코드를 고쳐 다시 제출하여서 AC를 받았다.
## 회전할 수 있는 경우는 총 8가지인데, 최단시간으로 도착점에 도달해야하므로 8가지 회전 경우의수 중에 몇가지는 필요가 없을 거라고 생각했지만
## 8가지 회전방향 모두 고려해주어야한다.

import heapq

## (x,y) 를 왼쪽위를 꼭짓점으로 하는 길이 2짜리 정사각형이 모두 0이면 회전 가능! --> 회전 경우의수 중 4가지
def upperLeftSquare(board, x, y):
    global N

    if x == N-1 or y == N-1:
        return False

    if board[x][y] == 0 and board[x+1][y] == 0 and board[x][y+1] == 0 and board[x+1][y+1] == 0:
        return True

    return False


## 정사각형의 아래에 위치한 좌우형태 --> 회전 경우의 수 중 2가지
def lowerHorizontal(board, x, y):
    global N

    if x == 0 or y == N-1:
        return False

    if board[x][y] == 0 and board[x-1][y] == 0 and board[x][y+1] == 0 and board[x-1][y+1] == 0:
        return True


    return False

## 정사각형의 오른쪽에 위치한 상하형태 --> 회전 경우의 수중 2가지
def righterVertical(board, x, y):
    global N

    if x == N-1 or y == 0:
        return False

    if board[x][y] == 0 and board[x+1][y] == 0 and board[x][y-1] == 0 and board[x+1][y-1] == 0:
        return True


    return False



def solution(board):
    global N
    
    ## 무한대 구현
    INF = int(1e9)

    N = len(board)

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]


    ## 우선순위 큐에서 이미 지나온 지점 반복을 피하기 위한 dp table을 INF로 초기화
    ## dp[x][y][dir] : (x,y) 지점을 기준으로 dir == 0 이면 좌우, dir == 1이면 상하로 배치되어 있음.
    dp = [[[INF for _ in range(2)] for _ in range(N)] for _ in range(N)]

    ## queue의 원소는 (cost, x, y, dir) 이다.
    queue = []

    dp[0][0][0]= 0
    heapq.heappush(queue,(0, 0,0,0))

    while queue:
        nowCost, x, y, DIR = heapq.heappop(queue)
        
        ## 도착점에 도달했을 경우 현재 최단경로를 리턴하기
        if (x == N -1 and y == N - 2 and DIR == 0) or (x == N-2 and y == N-1 and DIR == 1):
            return nowCost

        ## 현재 상황이 최단경로보다 클 경우는 무시하기!
        if dp[x][y][DIR] < nowCost:
            continue


        ## 이동하기
        for i in range(4):
            nx1 = x + dx[i]
            ny1 = y + dy[i]


            ## 좌우형태
            if DIR == 0:
                nx2 = x + dx[i]
                ny2 = y+1 + dy[i]

            ## 상하형태
            elif DIR == 1:
                nx2 = x+1 + dx[i]
                ny2 = y + dy[i]

                
            
            ## 범위를 벗어나면 무시하기!
            if not (0 <= nx1 < N and 0 <= ny1 < N and 0 <= nx2 < N and 0 <= ny2 < N):
                continue


            ## 둘다 빈칸이고,
            ## 지금까지 찾은 최단경로보다 작은 경우 업데이트하고 큐에 삽입하기
            if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:

                if dp[nx1][ny1][DIR] > nowCost + 1:
                    dp[nx1][ny1][DIR] = nowCost + 1
                    heapq.heappush(queue, (dp[nx1][ny1][DIR],nx1, ny1, DIR))
                
    
        ## 회전하기
        newCost = nowCost + 1
        
        if upperLeftSquare(board, x, y):

            ## 좌우형태
            if DIR == 0:

                if dp[x][y][1] > newCost:
                    dp[x][y][1] = newCost
                    heapq.heappush(queue, (dp[x][y][1], x, y, 1))

                if dp[x][y+1][1] > newCost:
                    dp[x][y+1][1] = newCost
                    heapq.heappush(queue, (dp[x][y+1][1], x, y+1, 1))
                    

            ## 상하형태
            elif DIR == 1:

                if dp[x][y][0] > newCost:
                    dp[x][y][0] = newCost
                    heapq.heappush(queue, (dp[x][y][0], x, y, 0))

                if dp[x+1][y][0] > newCost:
                    dp[x+1][y][0] = newCost
                    heapq.heappush(queue, (dp[x+1][y][0], x+1, y, 0))



        elif lowerHorizontal(board, x, y):

            ## 좌우형태
            if DIR == 0:

                if dp[x-1][y][1] > newCost:
                    dp[x-1][y][1] = newCost
                    heapq.heappush(queue, (dp[x-1][y][1], x-1, y, 1))


                if dp[x-1][y+1][1] > newCost:
                    dp[x-1][y+1][1] = newCost
                    heapq.heappush(queue, (dp[x-1][y+1][1], x-1, y+1, 1))

        elif righterVertical(board, x, y):
            
            ## 상하형태
            if DIR == 1:

                if dp[x][y-1][0] > newCost:
                    dp[x][y-1][0] = newCost
                    heapq.heappush(queue, (dp[x][y-1][0], x, y-1, 0))


                if dp[x+1][y-1][0] > newCost:
                    dp[x+1][y-1][0] = newCost
                    heapq.heappush(queue, (dp[x+1][y-1][0], x+1, y-1, 0))
