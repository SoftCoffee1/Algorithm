## 문제의 요구조건 그대로 구현을 해내가면 어렵지 않게 AC를 받을 수 있는 문제이다.
## 괄호의 종료가 1개여서 문제의 난이도가 낮았지만, 괄호의 종류가 여러개여도 dict 자료구조를 이용하여 같은 로직으로 풀 수 있을 것이다.

## 올바른 괄호 문자열이면 True, 아니면 False를 리턴하는 함수
def isCorrectString(s):

    count = 0

    for item in s:

        ## 열린괄호면 +1 하기
        if item == "(":
            count += 1

        ## 닫힌괄호면 -1 하기
        elif item == ")":
            count -= 1


        ## 중간과정에서 닫힌괄호의 개수가 더 많다면
        ## 올바른 괄호 문자열이 될 수 없다.
        if count < 0:
            return False



    ## 탐색이 다 완료되었다면, "(" 와 ")" 개수는 항상 같다는 조건에 의해 올바른 괄호 문자열이 된다.
    return True


## 4-4의 과정을 구현한 함수
## u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호방향을 뒤집은 문자열을 리턴하는 함수
def rev(u):

    result = ""

    for item in u[1:len(u)-1]:

        if item == "(":
            result += ")"

        else:
            result += "("

    return result
    


def process(p):

    ## 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if p == "":
        return ""

    
    ## 균형잡힌 괄호 문자열 판단을 위한 counter변수
    count = 0

    u = ""

    ## u, v를 구하는 과정
    for idx, item in enumerate(p):

        u += item
                    
        if item == "(":
            count += 1

        elif item == ")":
            count -= 1


        if count == 0:
            v = p[idx+1:]
            break


    
    ## u가 올바른 괄호 문자열이면
    if isCorrectString(u):
        return u + process(v)



    ## u가 올바른 괄호 문자열이 아니면
    else:
        return "(" + process(v) + ")" + rev(u)
        

def solution(p):


    answer = process(p)

    
    return answer
