# 원소들의 개수를 저장하는 dict가 필요하다면
## Counter의 사용을 생각해보자!!
## --> Counter.most_common() : 가장 많이 등장한 원소부터 차례로 정렬하여 리스트 리턴
from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    ## 세트메뉴를 구성하는 메뉴의 종류의 개수에 대해
    for courseNum in course:
        counterDict = []

        ## 각각의 주문에 대해서
        for order in orders:

            ## 만들 수 있는 조합을 모두 counterDict에 append하는 느낌.
            counterDict += combinations(sorted(order), courseNum)

        ## ********** key point ******* ##
        ## Counter를 이용해 각 원소의 개수를 센 후,
        ## most_common()을 이용해 많이 등장한 순서대로 정렬된 리스트를 반환 받음.
        counter = Counter(counterDict).most_common()

        ## 만들 수 있는 조합이 없는 경우에는 무시한다.
        if len(counter) == 0:
            break

        ## 가장 많이 선택받은 세트구성을 answer에 append해준다.
        nowNum = counter[0][1]
        for item, num in counter:
            if nowNum == num and num != 1:
                answer.append("".join(item))
            else:
                break

    ## 정답 배열을 사전순으로 정렬하라는 문제의 조건
    answer.sort()

    return answer
