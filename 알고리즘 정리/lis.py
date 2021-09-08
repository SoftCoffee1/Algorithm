## 가장 긴 증가하는 부분 수열 관련 모든 것!! (a.k.a longest increasing series : lis)

"""
1. lis의 길이를 구하는 문제
    --> dynamic programming을 이용 (O(N^2))
    --> binary search를 이용 (O(Nlog(N)))
    
    
    1. dynamic programming을 이용!! (time complexity : O(N^2))
        - N : 현재 주어진 수열의 길이
        - arr : 주어진 수열
        - dp[i] : arr[i]를 마지막 원소로 가지는 가장 긴 증가하는 부분수열의 길이 (모든 원소 1로 초기화해주기!!)
            --> ex. arr = [10, 20, 10, 30, 20, 50]
                     dp = [ 1,  2,  1,  3,  2,  4] --> 가장 피부에 와닿는 설명법이라고 생각함. 
                     
        - lis의 길이는 max(dp)이다.
        
        ####################실제 코드####################
        
        N = int(input().rstrip())
        arr = list(map(int, input().rstrip().split()))
        dp = [1 for _ in range(N)]
        
        for i in range(N):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        print(max(dp))
        
        ################################################
      
      
      
    2. binary search를 이용!! (time complexity : O(Nlog(N)))    --> 위의 방법보다 시간효율적인 방법이다!!
        - N : 현재 주어진 수열의 길이
        - arr : 주어진 수열
        - dp[i] : 길이가 i인 증가수열들의 마지막 값들 중의 최솟값
          --> ex. arr = [10, 20, 15, 25, 12, 20]
                   dp = [10, 12, 20] --> 1번 방법과는 달리 len(dp) 와 len(arr)가 다르다!!
                   
          --> bisect_left(dp, element) : dp가 정렬되어 있을때, 정렬을 깨뜨리지 않고 element가 끼워져 들어갈 수 있는 인덱스를 반환하는 함수.
                   
        - lis의 길이는 len(dp)이다.
        
        ####################실제 코드####################
        
        from bisect import bisect_left
        
        N = int(input().rstrip())
        arr = list(map(int, input().rstrip().split()))
        dp = [arr[0]]
        
        for i in range(N):
        
            if arr[i] > dp[-1]:
                dp.append(arr[i])
            
            else:
                idx = bisect_left(dp, arr[i])
                dp[idx] = arr[i]
                
        print(len(dp))
        
        ################################################


2. lis를 직접 구하는 문제
    --> dynamic programming을 이용 (O(N^2))
    --> binary search를 이용 (O(Nlog(N)))
    
    
    1. dynamic programming을 이용!!
        - N : 현재 주어진 수열의 길이 
        - arr : 주어진 수열
        - dp[i] : arr[i]를 마지막 원소로 가지는 가장 긴 증가하는 부분수열의 길이 (모든 원소 1로 초기화해주기!!)
        
        -----------------> 여기까지 정의된 상태로 dp를 구하는 것은 위의 lis의 길이만 구하는 과정이랑 같다.
        -----------------> 이 아래부터 lis 들 중 한가지를 직접 구하는 방법이다.
        -----------------> lis의 길이는 위와 같이 max(dp)
        
        
        --> max(dp)를 갖는 인덱스값에 해당하는 원소가 곧 lis의 가장 마지막원소가 될 것이다.
        --> lis의 가장 마지막 원소를 시작으로 dp를 앞으로 훑으면서
        --> 현재 찾는 dp의 값(max_dp)과 현재 탐색 원소의 dp값이 같다면 lis에 append 해주고 max_dp -= 1해준다.
        --> 매 루프마다 한칸씩 앞으로 가면서 탐색하는 것이므로 현재탐색 원소의 인덱스 (max_idx) -= 1 해준다.
        --> max_dp가 음수가 되는순간 루프 탈출!
        
        - max_dp : max(dp)의 값
        - max_idx : max(dp)의 인덱스값
        - lis : 가장 긴 증가하는 부분수열을 저장
        - 
        
        
        ####################실제 코드####################
        
        N = int(input().rstrip())
        arr = list(map(int, input().rstrip().split()))
        dp = [1 for _ in range(N)]
        
        for i in range(N):
            for j in range(i):
                dp[i] = max(dp[i], dp[j] + 1)
        
        max_dp = max(dp)
        max_idx = dp.index(max_dp)
        lis = []
        
        while max_dp >= 0:
            if dp[max_idx] == max_dp:
                lis.append(arr[max_idx])
                max_dp -= 1
                
            max_idx -= 1
            
        lis.reverse()
        print(*lis)
        
        ################################################
        
        
        
    2. binary search 이용!!
        - N : 현재 주어진 수열의 길이
        - arr : 주어진 수열
        - dp[i] : 길이가 i인 증가수열들의 마지막 값들 중의 최솟값
        - res[i] : arr[i]를 마지막 원소로 가지는 가장 긴 증가하는 부분수열의 길이 --> dynamic programming을 이용한 방법에서 가져온 배열
        
        -----> 기본적인 구조는 lis의 길이를 이분탐색으로 구하는 방법과 비슷하지만, res를 업데이트 해주는 과정이 추가된 것이다.
        -----> item > dp[-1] 인 경우에는, 현재의 dp의 길이가 곧 현재 원소를 마지막으로 하는 가장 긴 증가하는 부분수열의 길이가 된다.
        -----> 아닐 경우에는, item을 끼워넣을 인덱스를 찾은 후, 그 인덱스+1이 곧 현재 원소를 마지막으로 하는 가장 긴 증가하는 부분수열의 길이가 된다.
        -----> 이 과정이 끝난 후, 역추적하는 과정에서는 res를 기준으로 역추적하면 된다.
        
        ####################실제 코드####################
        
        from bisect import bisect_left
        
        N = int(input().rstrip())
        arr = list(map(int, input().rstrip().split()))
        dp = [arr[0]]
        res = [1]
        
        for item in arr[1:]:
        
            if item > dp[-1]:
                dp.append(item)
                res.append(len(dp))
            
            else:
                b_idx = bisect_left(dp, item)
                dp[b_idx] = item
                res.append(b_idx+1)
                    
        result = []
        len_dp = len(dp)
        
        for idx in range(len(res)-1,-1,-1):
            if res[idx] == len_dp:
                result.append(arr[idx])
                len_dp -= 1
              
        print(len(result))
        print(*result[::-1])
        
        ################################################
       
"""
