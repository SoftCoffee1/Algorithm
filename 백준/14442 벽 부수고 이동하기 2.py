# 14442 벽 부수고 이동하기 2
# https://www.acmicpc.net/problem/14442


## 카카오 2020 인턴 : 경주로 건설, 백준 1126 도로포장과 비슷한 류의 다차원 다익스트라 문제라고 인식하고, 풀이를 시도하였다.
## 두개의 풀이를 업로드 하였는데,
### 첫번째 풀이 : 다차원 다익스트라를 이용하여, 확정성이 있는 풀이.
### 두번째 풀이 : 이차원 배열과, 문제의 특성을 이용하여, 시간과 메모리를 단축 한 풀이.


## 첫번째 풀이
## 3차원 dp를 설정하여 지점과, 뚫고 온 벽의 개수를 모두 인수로 하는 리스트를 만들고, 그 값은 그러한 조건에서의 최단경로의 값을 저장하였다.
## 그러나, 가중치가 없는 그래프이기 때문에, 같은 루프를 도는 타이밍에는 모두 최단경로의 값이 같다.
## 여기서 최단경로값을 인수로 갖는 dp를 만들지 않고, 최단경로값을 queue에 매번 집어넣는 방법은 비효율적이라고 할 수 있다.
### 두번째 풀이는 이를 보완한 풀이이다.
from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)
    
N, M, K = map(int, input().rstrip().split())

MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().rstrip())))


## dp[x][y][k] : (x,y)에 k개의 벽을 뚫고 왔을 때의 최단 경로
dp = [[[INF for _ in range(K+1)] for _ in range(M)] for _ in range(N)]

## (x, y, k, distance)를 원소로 하는 큐
queue = deque()
queue.append((0, 0, 0, 1))

## (1,1) 까지의 최단경로는 1으로 초기화
for i in range(K+1):
    dp[0][0][i] = 1


dx = [1,-1,0,0]
dy = [0,0,1,-1]

# K개 이하로 벽 부수고 이동 가능 여부 저장 변수
possible = False

while queue:
    x, y, nowK, distance = queue.popleft()

    if x == N-1 and y == M-1:
        possible = True
        break

    ## 현재 경로가 dp에 저장된 최단 경로보다 큰 경우는 무시하기!
    if dp[x][y][nowK] < distance:
        continue


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]


        ## 범위에서 벗어난 경우는 무시하기!
        if not (0 <= nx < N and 0 <= ny < M):
            continue



        ## 벽인 경우
        if MAP[nx][ny] == 1:

            ## 현재 부순 벽의 개수가 k개 미만이면서 부수고 가는 경로가 더 짦으면 업데이트 한 후 큐에 삽입
            ### --> 벽 부수고 이동하기!
            if nowK < K and dp[nx][ny][nowK+1] > distance + 1:
                dp[nx][ny][nowK+1] = distance + 1
                queue.append((nx, ny, nowK+1, dp[nx][ny][nowK+1]))

            
            ## 현재 부순 벽의 개수가 k개인 경우
            ### --> 더 이상 벽을 부수는것은 불가능하므로, 무시하기!


        ## 벽이 아닌 경우
        ## 그쪽으로 가는 경로가 더 짧은 경로이면 업데이트 한 후 큐에 삽입
        elif MAP[nx][ny] == 0 and dp[nx][ny][nowK] > distance + 1:
            dp[nx][ny][nowK] = distance + 1
            queue.append((nx, ny, nowK, dp[nx][ny][nowK]))


if possible:
    print(distance)
else:
    print(-1)
    
    

## 두번째 풀이
## visited라는 이차원 배열을 설정하고, K+1로 초기화를 해놓는데, 각각의 위치에 부순 벽의 최소 개수를 저장하는 리스트이다.
## 어느 지점에 도달해야 할때, 무조건 더 부순 벽의 개수가 작은 상황이 최단경로를 만들어 줄 확률이 있기 때문이다.
## 이때문에 약간의 그리디 아이디어가 포함되어 있다고 말 할 수 있을 것 같다.

from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)
    
N, M, K = map(int, input().rstrip().split())

MAP = []
for _ in range(N):
    MAP.append(list(map(int, input().rstrip())))


## visited[x][y] : (x,y)를 몇개의 벽을 뚫고 왔는지 체크하는 2차원 리스트
visited = [[K+1 for _ in range(M)] for _ in range(N)]

## (x, y, k)를 원소로 하는 큐
queue = deque()
queue.append((0, 0, 0))

## (1,1)에는 벽 없이 도달 가능하다.
visited[0][0] = 0


dx = [1,-1,0,0]
dy = [0,0,1,-1]

# K개 이하로 벽 부수고 이동 가능 여부 저장 변수
possible = False

## 가중치가 없는 다익스트라이므로, queue에 길이 변수마저 생략할 수 있다.
distance = 1
while queue:

    l = len(queue)

    for _ in range(l):
        x, y, nowK = queue.popleft()

        if x == N-1 and y == M-1:
            possible = True
            break



        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            ## 범위에서 벗어난 경우는 무시하기!
            if not (0 <= nx < N and 0 <= ny < M):
                continue


            ## 어느 지점에 도달할 때, 부순 벽의 개수가 최소인 순간만 저장해도 된다. ##
            ## 빈칸이고, 더 적은 부순 벽으로 접근 가능한 경우만 업데이트 해주기!
            if MAP[nx][ny] == 0 and visited[nx][ny] > nowK:
                visited[nx][ny] = nowK
                queue.append((nx, ny, nowK))

            ## 벽이고, 더 적은 부순 벽으로 접근 가능하고, nowK가 K 미만인 겨우 업데이트 해주기!
            elif MAP[nx][ny] == 1 and visited[nx][ny] > nowK + 1 and nowK < K:
                visited[nx][ny] = nowK + 1
                queue.append((nx,ny,nowK+1))


    if possible:
            break
        
    distance += 1


if possible:
    print(distance)
else:
    print(-1)
