# 내가 한 방법으로 했을 시에는 뺄셈 처리하는 것이 조금 까다로운 문제였다.

# 1. 피연산자 2개와 연산자 1개를 앞에 - 있는것까지 모두 뽑아낸다.
# 2. num1 에 -가 딸려온 경우 --> expression의 가장 앞이면 실제로 음수인 것이고, 가장 앞이 아니라면, - 바로앞에있는 문자가 숫자면 양수이고, 연산자이면 음수인 것이다.
# 3. 이렇게 뽑아온 숫자 두개짜리 문자열을 compute 함수에 집어넣어 실제 연산을 진행하는데,
#    eval 함수를 실제로 구현한 함수가 compute 함수이다.
#    --> num1의 -는 처리가 끝났으므로 num2의 -를 처리해주면 끝이다.
#    --> 중간에 "-" 하나있으면 그냥 + 연산, 중간에 "--" 있으면 -연산을 하도록 구현하였다.
#    ----------> eval 연산을 이용하자면 77번째 줄에 compute(now) 대신 str(eval(nom))를 해주면 된다!

from itertools import permutations
import re


def compute(string):

    numParser = re.compile("[-]?[0-9]+")
    num1, num2 = map(int, numParser.findall(string))

    # 덧셈
    if "+" in string:
        return str(num1 + num2)

    # 곱셈
    elif "*" in string:
        return str(num1 * num2)

    # 뺄셈
    elif "-" in string:
        return str(num1 + num2)

    # 뺄셈
    elif "--" in string:
        return str(num1 - num2)
    

def solution(expression):
    answer = 0
    
    # 덧셈, 뺄셈, 곱셈 파싱기
    addParser = re.compile("[-]?[0-9]+[+][-]?[0-9]+")
    subParser = re.compile("[-]?[0-9]+[-][-]?[0-9]+")
    mulParser = re.compile("[-]?[0-9]+[*][-]?[0-9]+")


    Parsers = {1 : addParser, 2 : subParser, 3 : mulParser}

    for comb in permutations([1,2,3], 3):

        tempExpression = expression

        for i in comb:
            
            while True:

                now = Parsers[i].search(tempExpression)

                if now == None:
                    break
                    
                # 뺄셈 처리 과정! (대상 식의 첫번째 숫자 처리!)
                if now.group()[0] == "-":
                  
                    # 가장 앞이면 음수가 맞음
                    if now.start() == 0:
                        now = now.group()
                     
                    # 가장 앞이 아니라면
                    else:
                        
                        # 그 직전 문자가 숫자이면 양수
                        if "0" <= tempExpression[now.start()-1] <= "9":
                            now = now.group()[1:]
                        
                        # 아니면 음수이다.
                        else:
                            now = now.group()
                 
                # 뺄셈이 아닌 경우에는 그자체로 파싱해주면 됨.
                else:
                    now = now.group()

                tempExpression = tempExpression.replace(now, compute(now), 1)
                
        # 절댓값 처리 후 최댓값 업데이트
        now = abs(int(tempExpression))
        answer = max(answer, now)


    return answer

