# 16235 나무 재테크
# https://www.acmicpc.net/problem/16235


## 문제에 주어진 조건대로 묵묵히 구현해나가는 카카오, 삼성 sw의 전형적인 문제이다.
## 시간복잡도, 고려할 필요없이, 묵묵히 구현해나가면 된다.


import sys
input = sys.stdin.readline

## 봄, 여름 구현 함수
def springAndSummer():
    global LAND
    global TREEs
    global N


    for i in range(N):
        for j in range(N):
            TREEs[i][j].sort()
            newTree = []
            deadTrees = 0
            for age in TREEs[i][j]:

                ## 아직 먹을 수 있는 양분이 충분한 경우
                if age <= LAND[i][j]:
                    LAND[i][j] -= age
                    newTree.append(age+1)


                ## 먹을 수 있는 양분이 충분하지 않은 경우, 뒤의 나무들은 모조리 사망.
                ## 죽은 친구들의 나이의 절반이 양분으로 추가됨.
                else:
                    deadTrees += age // 2


            TREEs[i][j] = newTree
            LAND[i][j] += deadTrees


## 가을 구현 함수
def fall():
    global LAND
    global TREEs
    global N


    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]


    for i in range(N):
        for j in range(N):

            for age in TREEs[i][j]:

                ## 나이가 5의 배수이면 번식가능
                if age % 5 == 0:

                    for DIR in range(8):
                        ni = i + dx[DIR]
                        nj = j + dy[DIR]


                        ## 범위 벗어나면 무시하기
                        if not(0 <= ni < N and 0 <= nj < N):
                            continue


                        TREEs[ni][nj].append(1)



## 겨울 구현 함수
def winter():
    global LAND
    global A
    global N

    for i in range(N):
        for j in range(N):
            LAND[i][j] += A[i][j]




## 1년동안 벌어지는 일을 종합한 함수
def oneYearCycle():
    springAndSummer()
    fall()
    winter()



## 살아있는 나무 세기
def aliveCount():
    global TREEs
    global N

    counter = 0

    for i in range(N):
        for j in range(N):
            counter += len(TREEs[i][j])


    print(counter)

    

    

## 땅의 한변 크기, 나무의 개수, 나무 키울 햇수
N, M, K = map(int, input().rstrip().split())

## S2D2가 겨울에 추가할 양분을 저장한 리스트
A = []
for _ in range(N):
    A.append(list(map(int, input().rstrip().split())))


## 상도의 땅(양분은 5로 초기화)
LAND = [[5 for _ in range(N)] for _ in range(N)]

## 나무의 분포 현황
TREEs = [[[] for _ in range(N)] for _ in range(N)]


## 첫 나무 심기 구현
for _ in range(M):
    x, y, z = map(int, input().rstrip().split())

    TREEs[x-1][y-1].append(z)



## K년동안 같은 과정을 반복
for _ in range(K):
    oneYearCycle()



aliveCount()
