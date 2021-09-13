"""
누적합 알고리즘(prefix sum algorithm)
--> 주어진 수열에 대해서 수열의 값자체는 변화가 없는 상황에서 구간 합 쿼리가 여러번 등장하는 경우에 쓸 수 있다.
--> 매번 구간 합을 계산하는 naive한 방법은 O(N^2)에 풀리고, 누적합 알고리즘은 O(N)에 풀린다.

##################### 실제 코드 ##########################

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
S = [0] + arr                                    # --> 누적합 알고리즘을 구동시키기 위한 전처리 배열

for i in range(1,N+1):
    S[i] += S[i-1]

## arr배열의 i번째에서 j번째 수를 모두 더한 값을 구하는 문제. (1 <= i,j <= N)
i, j = map(int, input().rstrip().split())


## S배열을 이용하여 결과값을 구하는 과정
result = S[j] - S[i-1]
print(result)

"""




"""
<<관련 알고리즘>>
1. kedane's algorithm : finding maximum subarray in O(N)  : 백준 10211


"""
