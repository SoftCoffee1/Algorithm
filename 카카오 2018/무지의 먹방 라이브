import heapq

def solution(food_times, k):

    queue = []

    disabled = k
    nowLen = len(food_times)

    answer = 0
    
    for i in range(len(food_times)):
        heapq.heappush(queue, (food_times[i], i+1))

    previousTime = 0
    while queue:
        nowTime, num = heapq.heappop(queue)

        now = (nowTime - previousTime) * nowLen
        
        # 네트워크 장애가 발생하는 경우
        if disabled - now < 0:
            heapq.heappush(queue, (nowTime, num))
            queue.sort(key = lambda x : x[1])

            ## disabled 가 아닌 disabled%nowLen을 하는 이유
            ### -> disabled는 현재 남은 초로, 여러바퀴를 도는것이 가능하디.
            ####   따라서, 나눗셈 연산을 활용해 같은 반복을 줄이는 것이다.
            return queue[disabled%nowLen][1]

        # 아직 장애가 발생하지 않는 경우
        else:
            disabled -= now
            nowLen -= 1
            previousTime = nowTime

        

        
    
    
    answer = -1
    return answer



# main

food_times = [3, 1, 2]
k = 5

print(solution(food_times, k))
