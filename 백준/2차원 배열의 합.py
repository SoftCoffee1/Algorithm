## 2167 2차원 배열의 합
##https://www.acmicpc.net/problem/2167


## 2차원 누적합 구현하는 기본적인 문제

### 1차원 누적합의 경우에는..
## --> [0]을 가장 앞에 추가해주었었다.
## --> S[x]는 1번째부터 x번째까지의 합을 저장한다.
## --> i번째부터 j번째까지의 합은 S[j] - S[i-1] 이다. (i <= j)

### 2차원 누적합의 경우에는..
## --> 사각형의 가장 왼쪽, 가장 위쪽에 값이 0인 배열들을 추가해준 이후에 전처리 과정을 진행한다.
## --> S[x][y]는 (1,1)을 왼쪽 위 꼭짓점 (x,y)를 오른쪽 아래 꼭짓점으로 하는 직사각형의 모든 원소들의 합을 저장한다.
## --> (i,j) 부터 (x,y) 까지의 합은 S[x][y] - S[i-1][y] - S[x][j-1] + S[i-1][j-1] 이다. (i <= x and j <= y)


import sys
input = sys.stdin.readline


N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]\

## 1차원 누적합의 경우에는 [0]을 가장 앞에 추가해주었었다.
## 2차원 누적합의 경우에도 사각형의 가장 왼쪽, 가장 위쪽에 값이 0인 배열들을 추가해준 이후에 전처리 과정을 진행한다.
S = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        S[i][j] = arr[i-1][j-1]

## 전처리 과정은 아래와 같다.
## 1차원 누적합의 경우는 S[x]는 1번째부터 x번째까지의 합을 저장해놓듯이
## 2차원 누적합의 경우는 S[x][y]는 (1,1)을 왼쪽 위 꼭짓점 (x,y)를 오른쪽 아래 꼭짓점으로 하는 직사각형의 모든 원소들의 합을 저장한다.
for i in range(1,N+1):
    for j in range(1,M+1):
        S[i][j] += S[i-1][j] + S[i][j-1] - S[i-1][j-1]



K = int(input().rstrip())

for _ in range(K):
    i, j, x, y = map(int, input().rstrip().split())
     
    
    ## 1차원 누적합의 경우는 i번째부터 j번째까지의 합은 S[j] - S[i-1] 이다. (i <= j)
    ## 2차원 누적합의 경우는 (i,j) 부터 (x,y) 까지의 합은 S[x][y] - S[i-1][y] - S[x][j-1] + S[i-1][j-1] 이다. (i <= x and j <= y)
    result = S[x][y] - S[i-1][y] - S[x][j-1] + S[i-1][j-1]
    print(result)
