"""
누적합 알고리즘(prefix sum algorithm)
--> 주어진 수열에 대해서 수열의 값자체는 변화가 없는 상황에서 구간 합 쿼리가 여러번 등장하는 경우에 쓸 수 있다. --> 값의 차이가 발생하는 경우에는 세그먼트 트리를 이용한다.
--> 매번 구간 합을 계산하는 naive한 방법은 O(N^2)에 풀리고, 누적합 알고리즘은 O(N)에 풀린다. (1차원의 경우!)
--> 매 쿼리마다 n차원 배열의 naive한 계산은 O((배열의 길이)^n) 이지만, 누적합 알고리즘을 이용하면 O(1)만에 결과 도출이 가능하다.

########## python의 경우
########## from itertool import accumulate을 이용하면 시간단축 및 코드 길이 단축 가능!

### 1차원 누적합의 경우에는..
## --> [0]을 가장 앞에 추가해주었었다.
## --> S[x]는 1번째부터 x번째까지의 합을 저장한다.
## --> i번째부터 j번째까지의 합은 S[j] - S[i-1] 이다. (i <= j)

### 2차원 누적합의 경우에는..
## --> 사각형의 가장 왼쪽, 가장 위쪽에 값이 0인 배열들을 추가해준 이후에 전처리 과정을 진행한다.
## --> S[x][y]는 (1,1)을 왼쪽 위 꼭짓점 (x,y)를 오른쪽 아래 꼭짓점으로 하는 직사각형의 모든 원소들의 합을 저장한다.
## --> (i,j) 부터 (x,y) 까지의 합은 S[x][y] - S[i-1][y] - S[x][j-1] + S[i-1][j-1] 이다. (i <= x and j <= y)



##################### 1차원 누적합 실제 코드 ############################

from itertools import accumulate

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
S = [0] + list(accumulate(arr))                                  # --> 누적합 알고리즘을 구동시키기 위한 전처리 배열

## arr배열의 i번째에서 j번째 수를 모두 더한 값을 구하는 문제. (1 <= i,j <= N)
i, j = map(int, input().rstrip().split())


## S배열을 이용하여 결과값을 구하는 과정
result = S[j] - S[i-1]
print(result)

#######################################################################



##################### 2차원 누적합 실제 코드 ############################

from itertools import accumulate
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

## 사각형의 가장 왼쪽, 가장 위쪽에 값이 0인 배열들을 추가해준 이후에 전처리 과정을 진행한다.
## S[x][y]는 (1,1)을 왼쪽 위 꼭짓점 (x,y)를 오른쪽 아래 꼭짓점으로 하는 직사각형의 모든 원소들의 합을 저장한다. --> (x, y)는 x번째 행, y번째 열을 의미한다.(인덱스값이 아님!!)
S = [[0 for _ in range(N+1)]]
for _ in range(M):
    S.append([0]+list(map(int, input().rstrip().split())))
    
for i in range(1,N+1):
    S[i] = list(accumulate(S[i]))
   
for i in range(1,N+1):
    for j in range(1,M+1):
        S[i][j] += S[i-1][j]


## arr배열의 (i,j)부터 (x,y)까지의 수를 모두 더한 값을 구하는 문제. (i <= x and j <= y)
i, j, x, y = map(int, input().rstrip().split())
     
## S배열을 이용하여 결과값을 구하는 과정
result = S[x][y] - S[i-1][y] - S[x][j-1] + S[i-1][j-1]
print(result)

#######################################################################

"""




"""
<<관련 알고리즘>>
1. kedane's algorithm : finding maximum subarray in O(N)  : 백준 10211


"""
