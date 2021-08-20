## step1. 한변의 길이가 2*M + N - 2인 정사각형 모양의 2차원 리스트를 생성하여
## step2. 그 2차원 리스트의 중앙에 자물쇠를 위치 시킨다.
## step3. 열쇠로 2차원 리스트의 모든 위치에 가져다 대면서,
## step4. 자물쇠가 열리면 True, 열리지 않으면 열쇠를 다음 위치로 대서 같은 과정을 반복한다.
## step5. 모든 경우의 수를 다 따져보았는데도 열리지 않았을 시에 False이다.



## --> 문제 풀기 전에 차근차근 전체적인 로직을 생각해놓고, 그 로직이 맞는지, 예외 케이스는 어디서 발생하는지 등을 미리 파악한 후에 코딩에 들어가는 것이 실수나 오류가 날 확률이 적을 듯 하다.
## --> 또한, 주석을 적극적으로 사용하면서 현재 내가 구현하고 있는 게 무엇인지 명확하게 하도록 하자. 주석을 통해 디버깅시간이 단축될 수도 있다. 
## --> 주석을 자세히 쓰면서 하면 시간이 더 오래걸릴것 같은 느낌이지만 사실 시간이 적게 든다는 것을 명심하자!!


from copy import deepcopy


def rotate90(square):

    N = len(square)
    M = len(square[0])

    ret = [[0 for _ in range(N)] for _ in range(M)]


    for i in range(N):
        for j in range(M):
            ret[j][N-i-1] = square[i][j]

    return ret


def unlocked(key, x, y):
    global temp
    global N, M


    ## XOR 연산을 이용해 자물쇠와 열쇠의 상태 확인해주기
    for i in range(M):
        for j in range(M):
            temp[x+i][y+j] ^= key[i][j]




    for i in range(N):
        for j in range(N):
            ## 1이 아닌 부분이 등장한다면, 이번 열쇠의 위치는 실패한것!
            ## False를 리턴하기!
            if temp[i + M - 1][j + M - 1] == 0:
                return False


    ## 모두 1이라면 현재의 열쇠의 위치로 자물쇠를 열 수 있다는 의미이다!
    ## True 를 리턴하기!
    return True

    

    


def solution(key, lock):
    global temp
    global N, M
    
    answer = True

    ## 자물쇠와 열쇠의 한변의 길이
    N = len(lock)
    M = len(key)

    ## 한변의 길이가 2*M + N - 2인 정사각형 모양의 2차원 리스트 생성해주기
    SQUARE = [[0 for _ in range(2*M + N - 2)] for _ in range(2*M + N - 2)]

    ## 2차원 리스트의 중앙에 자물쇠 위치 시키기
    for i in range(N):
        for j in range(N):
            SQUARE[i + M - 1][j + M - 1] = lock[i][j]


    ## 열쇠 2차원 리스트의 모든 위치에 가져다 대면서 체크하기!

    ## 2*M + N - 2 짜리 2차원 리스트를 90도씩 4번 돌려본다.
    for rotate in range(4):

        ## 각각의 각도에서 모든 지점을 체크하기!
        for i in range(M+N-1):
            for j in range(M+N-1):
                temp = deepcopy(SQUARE)

                ## 현재 위치에서 열쇠를 끼워넣어봤더니 성공한 경우,
                ## 바로 True를 리턴해준다.
                if unlocked(key,i,j):
                    return True


        SQUARE = rotate90(SQUARE)
        


    ## 모든 상황을 다 살펴보았는데도 열 수 없었으므로 False를 리턴한다.
    return False
                
                
    
    
    return answer
