## well-known problem in Computer Science

## 10211 Maximum Subarray
## https://www.acmicpc.net/problem/10211



########################### 1. brute-force in O(N^2) ###########################
## prefix Sum을 위한 전처리 배열을 생성한 후
## 2중 for문을 돌면서 모든 가능성을 체크한다.

import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    S = [0] + arr

    for i in range(1,N+1):
        S[i] += S[i-1]

    maxVal = -1000
    for i in range(1, N+1):
        for j in range(i, N+1):
            now = S[j] - S[i-1]

            if now > maxVal:
                maxVal = now

    print(maxVal)
    
#################################################################################
    

########################### 2. Kedane's algorithm in O(N) ###########################
## prefix Sum을 위한 전처리 배열을 생성하는 과정에 약간의 아이디어를 추가한다.
## 배열의 원래 현재 값과, 직전의 값을 마지막값으로 하는 부분배열의 합의 최대값과 현재값을 더한 값을 비교하여, 더 큰값을 할당해주는 방법.

import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    arr = list(map(int, input().rstrip().split()))
    S = [0] + arr

    for i in range(1,N+1):
        S[i] = max(S[i], S[i-1] + S[i])

    print(max(S[1:]))
    
######################################################################################
