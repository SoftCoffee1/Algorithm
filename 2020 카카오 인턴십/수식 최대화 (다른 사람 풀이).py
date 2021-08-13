from itertools import permutations
import re


def solution(expression):

    # expressions에 3가지 연산자가 모두 들어있지 않을 수도 있으므로 있는 것들만으로 우선순위 체크하기!
    # 6가지 다 돌려보는 것보다 시간이 절약되는 테크닉이다.
    expressions = set(re.findall("\D", expression))
    prior = permutations(expressions)

    # 식의 결과 값들을 저장하는 리스트
    cand = []

    
    for op_cand in prior:
        # 정수가 아닌 애들과 정수인 애들로 나눈다음,
        # 그것들을 split 해서 리스트형태로 temp변수에 저장한다.
        temp = re.compile("(\D)").split(expression)
        for exp in op_cand:

            # exp 연산자가 있을 때만 루프를 돈다.
            while exp in temp:
                
                # exp 연산자가 있는 가장 앞 인덱스를 idx에 저장한다.
                idx = temp.index(exp)

                # 현재 찾은 인덱스를 기준 양 옆의 숫자들을 이용해 계산을 하고, 그 바깥부분은 그대로 놔두면서 temp를 업데이트 해준다.
                temp = temp[:idx-1] + [str(eval(''.join(temp[idx-1:idx+2])))] + temp[idx+2:]


        # 현재 연산자 우선순위일때의 값을 cand에 append 해준다.
        cand.append(abs(int(temp[0])))
    return max(cand)
