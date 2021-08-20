## 카카오의 전형적인 1번문제처럼, 쉬운 구현문제였다.
## 길이 1짜리 문자열을 처리해줄때 약간의 오류가 있었다. 극히 일부의 테케를 통과하지 못하는 것이라면 특이점(시작, 끝 부분)을 확인해보자!

def make(s, number):

    ## 결과 문자열 저장
    result = ""

    ## 현재 탐색 문자열의 반복 횟수 저장 변수
    count = 1
    for i in range(0, len(s), number):

        ## 현재 탐색 문자열과 다음 탐색 문자열이 같다면
        ## --> count를 늘려주고, 계속 탐색하기
        if s[i:i+number] == s[i+number:i+2*number]:
            count += 1
            
        ## 현재 탐색 문자열과 다음 탐색 문자열이 다르다면
        ## --> count == 1이면 문자열에 그냥 추가
        ## --> count > 1 이면 반복횟수 + 문자열을 추가
        ## 그리고 count는 1로 초기화 해주기!
        else:

            if count == 1:
                result += s[i:i+number]

            else:
                result += str(count) + s[i:i+number]


            count = 1


    ## 최소 길이 문자열을 찾는 것이므로 현재 단위로 만들었을때의 길이를 리턴
    return len(result)
    




def solution(s):

    ## 하나도 압축되지 않을때의 최대 길이는 1000이므로 1001을 무한대의 의미로 사용해도 된다.
    answer = 1001

    ## 단위는 전체 문자열 길이의 절반까지만 체크해보아도 된다. (절반에서 하나 큰 부분까지 살피는 이유는 길이가 1짜리 문자열일 경우를 커버해줘야 하기 때문이다.)
    ## 그 이후까지 넘어가게 되면 더 이상 반복되는 부분이 없기 때문!
    for number in range(1,len(s)//2 + 2):
        answer = min(answer , make(s, number))
    
    return answer
