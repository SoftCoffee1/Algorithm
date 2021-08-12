############################################### parametric search #######################################################


#" 최적화 문제를 결정 문제로 변환!" 하여 문제를 해결하는 기법

#정답의 대상들을 정렬하였을 때, 조건을 만족하는 대상들과 아닌 대상들이 어느 한 경계점을 기준으로 두 부분으로 나뉘는 상황에 활용가능!



########### 1. 최댓값 파라메트릭 서치  ----------> 왼쪽부분에 정답 존재!

def parametric_search_max(arr):

    start = 1
    end = max(arr)

    # 무한루프는 start == end 일 경우에 빠져나오게 된다!
    while start < end:
       
       
        mid = (start + end + 1) // 2

        if condition(mid):
            start = mid

        else:
            end = mid - 1
        

    return start
    
    
    
    
########### 2. 최솟값 파라메트릭 서치  ----------> 오른쪽부분에 정답 존재!

def parametric_search_min(arr):

    start = 1
    end = max(arr)

    # 무한루프는 start == end 일 경우에 빠져나오게 된다!
    while start < end:
       
       
        mid = (start + end) // 2

        if condition(mid):
            end = mid

        else:
            start = mid + 1
        

    return start
