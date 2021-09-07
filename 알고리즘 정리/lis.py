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
    
    
    1. dynamic programming을 이용!! ()
