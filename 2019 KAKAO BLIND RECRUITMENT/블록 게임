# 블록 게임


# 하라는대로 구현만 잘 해주면 맞출 수 있는 문제. --> 카카오 스타일의 완전탐색 문제!
# shape을 저장하는 배열에서 각각의 모양을 손으로 짰다,, 손으로 정교한 작업을 직접 진행할 때는 그 부분에서 실수 할 부분이 가장 크므로, 최선을 다해 실수하지 않도록 꼼꼼히 확인하기!

########## ****손으로 정교한 작업을 할때는 아주 꼼꼼히 하자.. 처음에 실수해놓으면 디버깅 시간이 무한대로 발산한다,,**** ##########3

from collections import deque
from copy import deepcopy

"""
# 이차원 배열 출력 함수 (문제 중간과정 점검에 필요!)
def printArr(arr):
    n = len(arr)
    m = len(arr[0])

    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()
    print()
"""


# 제거 가능성이 있는 블록 판별하고, 그 블록을 실제로 제거할 수 있는지 판별하여, 제거 가능하면 제거하고 True를 리턴, 제거 불가능하면 False를 리턴하는 함수!
def possible_shape(x, y):
    global BOARD
    global shape
    global N

    # 현재 블럭의 번호
    blockNum = BOARD[x][y]


    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    queue = deque()
    queue.append((x,y))

    # 블럭의 원형을 비교하기 위해 x값과 y값의 최소를 저장하는 변수
    minX = x
    minY = y

    # 현재 블럭의 실제 형태 저장하는 리스트
    block = [[x,y]]

    # 블럭 저장하기
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            if not (0 <= nx < N and 0 <= ny < N):
                continue

            inside = False
            if BOARD[nx][ny] == blockNum:
                for ii, jj in block:
                    if ii == nx and jj == ny:
                        inside = True
                        break

                if inside:
                    continue
                
                block.append([nx,ny])
                minX = min(minX, nx)
                minY = min(minY, ny)
                queue.append((nx,ny))


    # 블럭의 실제형태를 통해 블럭의 원형을 도출해내기
    blockPrototype = deepcopy(block)
    for i in range(len(block)):
        blockPrototype[i][0] -= minX
        blockPrototype[i][1] -= minY
        blockPrototype[i] = tuple(blockPrototype[i])

    # shape의 원소들과 비교하기 위해 정렬해주기
    blockPrototype.sort()

    

    # shape에 있는 블럭의 모양들과 현재 블럭의 모양이 일치하면, 본인 위에 있는 블럭이 가로막고 있지 않은 지 체크 후, 없으면 검은 블록이 내려올 수 있으므로 삭제가 가능하다!
    for i in range(len(shape)):
        if shape[i][0] == blockPrototype:
            #print(shape[i][0], blockPrototype)

            
            x1 = minX + shape[i][1][0][0]
            y1 = minY + shape[i][1][0][1]

            x2 = minX + shape[i][1][1][0]
            y2 = minY + shape[i][1][1][1]


            # 현재 모양의 빈공간들에 다른 블럭들이 차지하고 있지 않을때,
            if BOARD[x1][y1] == 0 and BOARD[x2][y2] == 0:

                # 첫번째 빈공간 위에 다른 블록이 있는 지 확인
                for a in range(x1):
                    if BOARD[a][y1] != 0:
                        return False

                # 두번째 빈공간 위에 다른 블록이 있는 지 확인
                for b in range(x2):
                    if BOARD[b][y2] != 0:
                        return False



                # 블록 삭제가 가능하므로 삭제한다
                for x, y in block:
                    BOARD[x][y] = 0

                return True

    return False
    
    

def solution(board):
    global BOARD
    global shape
    global N
    global answer

    BOARD = deepcopy(board)
    
    N = len(board)

    # 제거가 가능한 블록들의 shape
    # 블록 모양, 직사각형을 채우기 위한 나머지 공간
    # 이런 류의 작업을 할때는, 집중하여 꼼꼼히 하기!!!!
    shape = [
        [[(0,0), (1,0), (1,1), (1,2)], [(0,1), (0,2)]],
        [[(0,1), (1,1), (2,0), (2,1)], [(0,0), (1,0)]],
        [[(0,0), (1,0), (2,0), (2,1)], [(0,1), (1,1)]],
        [[(0,2), (1,0), (1,1), (1,2)], [(0,0), (0,1)]],
        [[(0,1), (1,0), (1,1), (1,2)], [(0,0), (0,2)]]
       ]


    answer = 0
    
    while True:
        done = False
        for i in range(N):
            for j in range(N):
                if BOARD[i][j] != 0:
                    #print(i, j)

                    # 삭제가 가능하다면, 삭제 후 다시 가장 위 (0,0)의 위치부터 다시 탐색하는 루프(그 자리에서부터 탐색하면 놓치는 것들 생김!)
                    if possible_shape(i,j):
                        answer += 1
                        done = True
                        break


            if done:
                break


        if not done:
            break

        
    
    return answer
