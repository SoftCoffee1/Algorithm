# 15683 감시
# https://www.acmicpc.net/problem/15683

###################### 첫번째 풀이는 cctv수가 최대 8대이고, 가질 수 있는 방향은 최대 4개 이므로 4^8 = 65536번 브루트포스 방식으로 다 돌려보는 것 ######################
####### 그러나 모든 cctv가 4개의 방향을 가지는 것은 아니기 때문에 위의 방법은 굉장히 중복이 많다. 더욱 최적화가 가능하다는 의미이다.

"""
1. CCTV 위치 확인
2. product함수를 이용해 각 CCTV의 방향 설정 후
3. 커버 영역 확인하기 --> spread 함수 이용하기
4. 커버 되지 않은 영역 개수 세기 --> count함수를 이용하기
"""


from itertools import product
from copy import deepcopy
import sys
input = sys.stdin.readline


## 한줄 쭉 커버하는 영역 #로 칠하는 함수
## spread함수 안에서 여러번 쓰일 함수
def spreadOnce(x, y, direction):
    global tempROOM
    global N, M

    ## 0 : 3시방향
    ## 1 : 6시방향
    ## 2 : 9시방향
    ## 3 : 12시방향
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    ## 퍼져나갈 위치를 담는 변수
    nx = x
    ny = y
    
    while True:
        nx += dx[direction]
        ny += dy[direction]


        ## 범위 벗어나면 더이상 못 퍼져나가므로 함수 종료
        if not (0 <= nx < N and 0 <= ny < M):
            return


        ## 벽(6)을 만나면 더이상 못 퍼져나가므로 함수 종료
        if tempROOM[nx][ny] == 6:
            return


        ## 빈칸이나 #를 만나면 계속 뻗어나가도 상관없음
        tempROOM[nx][ny] = "#"
    

    


## 각각의 cctv가 커버하는 영역을 #로 칠하는 함수
def spread(x, y, Type, direction):
    global tempROOM


    ## 1번 cctv
    if Type == 1:
        spreadOnce(x, y, direction)
        

    ## 2번 cctv
    elif Type == 2:
        spreadOnce(x, y, direction)
        spreadOnce(x, y, (direction + 2)%4)

    ## 3번 cctv
    elif Type == 3:
        spreadOnce(x, y, direction)
        spreadOnce(x, y, (direction + 1)%4)

    ## 4번 cctv
    elif Type == 4:
        spreadOnce(x, y, direction)
        spreadOnce(x, y, (direction + 1)%4)
        spreadOnce(x, y, (direction + 2)%4)

    ## 5번 cctv
    elif Type == 5:
        spreadOnce(x, y, direction)
        spreadOnce(x, y, (direction + 1)%4)
        spreadOnce(x, y, (direction + 2)%4)
        spreadOnce(x, y, (direction + 3)%4)


## 현재 사무실의 사각지대 영역의 수를 세는 함수
def count(arr):
    global N, M

    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                result += 1

    return result
    
    
## 세로크기, 가로크기
N, M = map(int, input().rstrip().split())

## 사무실 정보
ROOM = []
CCTVs = []
for i in range(N):
    ROOM.append(list(map(int, input().rstrip().split())))

    for j in range(M):

        # CCTV 발견했을 시, 위치 및 타입 저장하고 사각지대가 아니라고 생각하기.
        if 1 <= ROOM[i][j] <= 5:
            CCTVs.append((i,j,ROOM[i][j]))
            ROOM[i][j] = "#"


## 사각 지대의 최소 크기 저장 변수(사무실의 칸이 최대 64칸 이므로 INF = 65로 설정!)
minVal = 65


## CCTV들의 모든 방향의 가능성을 브루트 포스방식으로 탐색하기
for DIRS in product([0,1,2,3], repeat = len(CCTVs)):

    ##사무실의 정보를 계속 바꿀거라, 그 다음 가능성을 탐색하기 용이하기 위해 따로 저장해서 탐색한다.
    tempROOM = deepcopy(ROOM)

    ## 각각의 CCTV들에 대해
    for i in range(len(CCTVs)):
        x, y, Type = CCTVs[i]
        direction = DIRS[i]

        ## 그 상태로 커버영역 체크하기
        spread(x, y, Type, direction)


    ## 최솟값을 갱신해주기
    minVal = min(minVal, count(tempROOM))


## 정답 출력
print(minVal)
        
    
################################## 두번째 방법 --> 첫번째 방법의 중복을 보완한 풀이! ##################################


"""
1. 0인 구간들 세기 --> 전체 0에서 cctv가 커버 가능한 여역을 빼면 정답이기 때문!
2. 각각의 cctv에 대해 커버 가능한 좌표들을 cctvs_case에 집합형태로 저장하기
3. dfs를 활용해 모든 조합을 체크하기!
"""

def watch(x, y, direction):
    ret = set()

    for d in direction:
        new_x, new_y = x + dx[d], y + dy[d]

        ## 범위를 벗어나면 종료
        while 0 <= new_x < N and 0 <= new_y < M:

            ## 벽을 만나면 그만 나아가기
            if office[new_x][new_y] == 6:
                break

            ## 빈칸이면 퍼져나갈 수 있는 곳이므로 추가하기
            if office[new_x][new_y] == 0:
                ret.add((new_x, new_y))

            new_x, new_y = new_x + dx[d], new_y + dy[d]


    return ret


def dfs(n, watched_set):
    global max_watched_cnt

    if n == len(cctvs_cases):
        if max_watched_cnt < len(watched_set):
            max_watched_cnt = len(watched_set)

        return

    for cctv_cases in cctvs_cases[n]:
        dfs(n+1, watched_set | cctv_cases)


## cctv가 가능한 케이스
cctvs_cases = []

## 방향은 동서남북 순서
dx, dy = (-1,0,1,0), (0,1,0,-1)

N, M = map(int, input().rstrip().split())
office = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 0인 구간들을 세는 변수
will_watched_cnt = 0

for idx in range(N*M):
    i, j = divmod(idx, M)

    ## 빈칸이면 개수 세기
    if office[i][j] == 0:
        will_watched_cnt += 1

    ## 1번 cctv
    elif office[i][j] == 1:
        cctvs_cases.append([watch(i,j,[v]) for v in range(4)])

    ## 2번 cctv
    elif office[i][j] == 2:
        cctvs_cases.append([watch(i,j, [v, (v+2)%4]) for v in range(2)])

    ## 3번 cctv
    elif office[i][j] == 3:
        cctvs_cases.append([watch(i,j,[v, (v+1)%4]) for v in range(4)])

    ## 4번 cctv
    elif office[i][j] == 4:
        cctvs_cases.append([watch(i,j,[v, (v+1)%4, (v+2)%4]) for v in range(4)])

    ## 5번 cctv
    elif office[i][j] == 5:
        cctvs_cases.append([watch(i,j,[0,1,2,3])])


## 최대 cctv영역 저장하는 변수
max_watched_cnt = 0


## 감시 가능한 최대 영역 개수를 구하는 과정
dfs(0, set())

## 최소 사각지대 개수
print(will_watched_cnt - max_watched_cnt)

