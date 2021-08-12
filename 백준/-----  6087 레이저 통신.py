# 6087 레이저 통신
# https://www.acmicpc.net/problem/6087


# 1. 꺽은 횟수를 우선순위 큐에 집어넣고 루프 돌리기!
# 2. 각 지점들 방문처리 타이밍때문에 한참동안 못풀었던 문제이다!
# -----> 큐에 집어넣을때 방문처리를 하지 않고, 큐에서 꺼낼때 방문처리를 해주어야 길을 막지 않는다!

import heapq
import sys
input = sys.stdin.readline


## MAP 출력 함수
def printArr(arr):
    n = len(arr)
    m = len(arr[0])

    for i in range(n):
        for j in range(m):
            if type(arr[i][j]) == str:
                print("%2s" %(arr[i][j]), end="  ")
            else:
                print("%2d" %(arr[i][j]), end="  ")
        print()

    print()




W, H = map(int, input().rstrip().split())

# 레이저의 시작점과 도착점 저장 리스트
Cs = []

MAP = []
for i in range(H):
    now = list(input().rstrip())
    MAP.append(now)

    for j in range(W):
        
        # C가 발견되면 이동 가능한 지점으로 만들어놓고, Cs 배열에 집어넣는다!
        if MAP[i][j] == "C":
            MAP[i][j] = "."
            Cs.append((i,j))


## 아래의 direction의 인덱스와 같게 설정해놓음!
dx = [0,1,0,-1]
dy = [1,0,-1,0]

startX = Cs[0][0]
startY = Cs[0][1]


# direction
# --> 4 : 시작
# --> 0 : 3시
# --> 1 : 6시
# --> 2 : 9시
# --> 3 : 12시

queue = []
heapq.heappush(queue, (-1, startX, startY, 4))


while queue:
    turn, x, y, way = heapq.heappop(queue)

    if x == Cs[1][0] and y == Cs[1][1]:
        break
    
    # 방문처리는 큐에서 꺼낼때 하기!!!!
    # 큐에 집어넣는 과정에서 방문처리를 하게되면 길을 막게 될 수도 있음.. --> 큐에 집어넣는 순서가 존재하기 때문!!
    # 큐에 집어넣을때는 여러가지 거울의 개수를 가지고 그 지점에 도달하게 되는 것을 다 판단하는것인데, 만약 거울개수가 같은 여러가지 점이 최단거리를 지나는 경로를 침범하게 될 수도 있다.
    # 큐에서 꺼내는 과정은 무조건 최소거울개수!
    
    
    ##### 의문점 ... 
    # 여기 if MAP[x][y] == "V":
    #          continue
    # 를 하면 왜 안되는거지 도대체???????????????????????????????????????????
    
    MAP[x][y] = "V"


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 밖이면 무시하기!
        if not (0 <= nx < H and 0 <= ny < W):
            continue


        if MAP[nx][ny] == ".":
            
            # 현재 머리방향과 이동방향이 같은 경우 --> turn 의 값은 그대로
            if i == way:
                heapq.heappush(queue, (turn, nx, ny, i))
                
            # 현재 머리방향과 이동방향이 다른 경우 --> turn 의 값에 1 추가
            else:
                heapq.heappush(queue, (turn + 1, nx, ny, i))
             
             
print(turn)
