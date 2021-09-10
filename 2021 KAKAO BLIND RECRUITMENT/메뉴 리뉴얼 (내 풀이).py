## 완전 탐색을 위한 거의 필수적이라고 할 수 있는 라이브러리
from itertools import combinations

def solution(orders, course):

    ## 정답 저장 배열
    answer = []

    ## 각각의 세트메뉴가 몇번 등장했는지를 저장하는 딕셔너리 (여기서 세트메뉴는 두번이상 선택받아졌고, 구성하는 음식종류가 course의 원소와 일치하는 경우가 있을때만 저장한다.)
    ansDict = {}

    ## ## 2중 for문을 통해 두사람을 순서없이 뽑는 과정을 구현하고,
    for i in range(len(orders)):
        for j in range(i+1, len(orders)):

            ## 그렇게 뽑힌 두 사람들이 공통으로 시킨 메뉴를 intersection 에 저장한다.
            intersection = set(orders[i]) & set(orders[j])

            
            ## 세트메뉴를 구성하는 음식종류는 최소 2종류므로 그보다 작은 경우는 무시한다.
            if len(intersection) >= 2:

                ## course의 각 원소에 대해 교집합의 크기와 크기 비교를 하는데
                for courseNum in course:

                    ## course원소 <= 교집합크기 --> 조합을 만들어 ansDict에 저장한다.
                    ## course원소 >  교집합크기 --> 조합 만들기가 불가능이므로 무시한다. (ex. 교집합이 "ABC" 이면 이들로 4개 이상의 메뉴로 구성된 세트메뉴는 만들 수 없다.)
                    if courseNum <= len(intersection):

                        for comb in combinations(intersection, courseNum):
                            comb = "".join(sorted(list(comb)))
                            
                            if comb not in ansDict:
                                ansDict[comb] = {i, j}

                            else:
                                ansDict[comb] |= {i, j}
                                

    ## ans : ansDict의 key값들로 구성된 리스트
    ## ans를 그 메뉴가 구성하는 음식 종류는 오름차순, 그 메뉴를 선택한 사람 수는 내림차순으로 정렬한다.
    ## ans배열 뭔지 모르겟으면 아래 print문 주석 제거해보기.
    ans = list(ansDict.keys())
    ans.sort(key=lambda x : (len(x), -len(ansDict[x])))
    #print(ans) 


    ## ans를 훑어보면서 현재 setMenu가 선택가능하다고 판단되면 answer배열에 추가, 아니면 무시하기!
    i = 0
    numOfPeople = len(ansDict[ans[0]])
    for setMenu in ans:

        if len(setMenu) == course[i]:
            if numOfPeople == len(ansDict[setMenu]):
                answer.append(setMenu)

        else:
            answer.append(setMenu)
            i += 1
            numOfPeople = len(ansDict[setMenu])
            

    ## 정답 배열을 사전순으로 정렬해서 출력하라는 문제의 조건
    answer.sort()

    ## 정답 반환!
    return answer
